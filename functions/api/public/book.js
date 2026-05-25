// POST /api/public/book — customer self-books a consultation slot
import { json, hashIp } from "../../_lib/auth.js";
import { genToken } from "../../_lib/tokens.js";
import { upsertContact, recordActivity } from "../../_lib/db.js";
import { sendEmail, brandedEmail, escapeHtml } from "../../_lib/email.js";
import { buildIcs } from "../../_lib/ical.js";
import { fmtPretty } from "../../_lib/dates.js";

const SITE_URL = "https://statelyshades.com";

export async function onRequestPost(context) {
  const { DB, env } = context.env ? { DB: context.env.DB, env: context.env } : context;
  const body = await context.request.json().catch(() => ({}));
  const required = ["start_at", "name", "email", "phone"];
  for (const k of required) {
    if (!body[k]) return json({ error: `Missing ${k}` }, 400);
  }
  const startAt = body.start_at;
  const dur = parseInt(body.duration_min || 60, 10);
  const endAt = computeEndIso(startAt, dur);

  // Re-check the slot is still free
  const conflict = await DB
    .prepare(`SELECT id FROM appointments
              WHERE status IN ('pending','confirmed') AND start_at < ?1 AND end_at > ?2`)
    .bind(endAt, startAt)
    .first();
  if (conflict) return json({ error: "Slot is no longer available — please pick another." }, 409);

  // Check it's within an active rule + not blocked
  const rules = (await DB.prepare(`SELECT * FROM availability_rules WHERE active=1`).all()).results || [];
  const dowJs = new Date(startAt + "Z").getUTCDay();
  const minute = parseInt(startAt.slice(11, 13), 10) * 60 + parseInt(startAt.slice(14, 16), 10);
  const inRule = rules.some((r) => r.day_of_week === dowJs && minute >= r.start_minute && minute + dur <= r.end_minute);
  if (!inRule) return json({ error: "Outside booking hours." }, 400);

  const blocks = await DB
    .prepare(`SELECT 1 FROM availability_blocks WHERE start_at < ?1 AND end_at > ?2 LIMIT 1`)
    .bind(endAt, startAt).first();
  if (blocks) return json({ error: "Slot is unavailable." }, 409);

  // Upsert contact
  const contactId = await upsertContact(DB, {
    name: body.name,
    email: body.email,
    phone: body.phone,
    address: body.address || null,
  });

  // Insert appointment
  const cancelToken = genToken(16);
  const ipHash = await hashIp(context.request.headers.get("CF-Connecting-IP"));
  const r = await DB
    .prepare(
      `INSERT INTO appointments (contact_id, type, start_at, end_at, duration_min, status, source,
        name, email, phone, site_address, rooms, notes, cancel_token)
       VALUES (?1, 'consultation', ?2, ?3, ?4, 'confirmed', 'web', ?5, ?6, ?7, ?8, ?9, ?10, ?11)
       RETURNING id`
    )
    .bind(
      contactId,
      startAt,
      endAt,
      dur,
      body.name,
      body.email,
      body.phone,
      formatAddress(body.address),
      body.rooms || null,
      body.notes || null,
      cancelToken,
    )
    .first();

  await recordActivity(DB, {
    entityType: "appointment", entityId: r.id, action: "booked",
    actorKind: "customer", actorName: body.name,
    details: { ip_hash: ipHash },
  });

  // Build iCal
  const ics = buildIcs({
    uid: `appt-${r.id}@statelyshades.com`,
    start: startAt, end: endAt,
    summary: `Stately Shades · In-Home Consultation`,
    description: `Free consultation with Stately Shades.\\n\\nQuestions? Call 629-298-8241.\\n\\nReschedule or cancel: ${SITE_URL}/book/?cancel=${cancelToken}`,
    location: formatAddress(body.address) || "Your home",
    organizer: "hello@statelyshades.com",
    organizerName: "Stately Shades",
    url: `${SITE_URL}/book/?cancel=${cancelToken}`,
  });

  // Send confirmation email to customer
  await sendEmail(context.env, {
    to: body.email,
    subject: `Your consultation is confirmed — ${fmtPretty(startAt)}`,
    html: brandedEmail({
      title: "You're confirmed.",
      preheader: `In-home consultation on ${fmtPretty(startAt)}.`,
      body: `
        <p>Hi ${escapeHtml(body.name.split(" ")[0])},</p>
        <p>Your free in-home consultation with Stately Shades is booked for:</p>
        <p style="font-size:18px;color:#14110D;font-weight:600;margin:14px 0">${escapeHtml(fmtPretty(startAt))}</p>
        ${body.address ? `<p>We'll come to:<br/><strong>${escapeHtml(formatAddress(body.address))}</strong></p>` : ""}
        ${body.rooms ? `<p><strong>Rooms / scope:</strong> ${escapeHtml(body.rooms)}</p>` : ""}
        <p>We'll bring samples, measure every window, and leave you with a written quote on the visit — no obligation. The whole visit usually takes 45–75 minutes depending on window count.</p>
        <p>If anything changes, you can <a href="${SITE_URL}/book/?cancel=${cancelToken}">reschedule or cancel here</a>, or just call/text us at <a href="tel:+16292988241">629-298-8241</a>.</p>
        <p style="margin-top:24px">Looking forward to meeting you,<br/>— Stately Shades</p>
      `,
    }),
    text: `Your consultation is confirmed for ${fmtPretty(startAt)}.\n\n` +
      (body.address ? `We'll come to:\n${formatAddress(body.address)}\n\n` : "") +
      `Reschedule/cancel: ${SITE_URL}/book/?cancel=${cancelToken}\n` +
      `Questions: 629-298-8241\n`,
    attachments: [{
      filename: "stately-shades-consultation.ics",
      contentType: "text/calendar; method=REQUEST",
      content: btoa(ics),
    }],
  });

  // Notify the team
  await sendEmail(context.env, {
    to: env?.STAFF_EMAIL || "hello@statelyshades.com",
    subject: `New booking · ${body.name} · ${fmtPretty(startAt)}`,
    html: brandedEmail({
      title: "New consultation booked.",
      body: `
        <p><strong>${escapeHtml(body.name)}</strong></p>
        <p>${escapeHtml(body.email)} · ${escapeHtml(body.phone || "")}</p>
        <p><strong>When:</strong> ${escapeHtml(fmtPretty(startAt))}</p>
        ${body.address ? `<p><strong>Where:</strong> ${escapeHtml(formatAddress(body.address))}</p>` : ""}
        ${body.rooms ? `<p><strong>Rooms:</strong> ${escapeHtml(body.rooms)}</p>` : ""}
        ${body.notes ? `<p><strong>Notes:</strong> ${escapeHtml(body.notes)}</p>` : ""}
        <p><a href="${SITE_URL}/crm/calendar.html">Open the calendar →</a></p>
      `,
    }),
    replyTo: body.email,
  });

  return json({ ok: true, id: r.id, cancel_token: cancelToken });
}

function computeEndIso(startIso, durMin) {
  const [d, t] = startIso.split("T");
  const [h, m] = t.split(":").map((n) => parseInt(n, 10));
  let total = h * 60 + m + durMin;
  const eh = Math.floor(total / 60);
  const em = total % 60;
  const pad = (n) => String(n).padStart(2, "0");
  return `${d}T${pad(eh)}:${pad(em)}:00`;
}

function formatAddress(a) {
  if (!a) return null;
  const parts = [a.street, a.city, a.state, a.zip].filter(Boolean);
  return parts.length ? parts.join(", ") : null;
}
