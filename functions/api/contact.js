// POST /api/contact — receives the consultation form and emails it to
// hello@statelyshades.com via Purelymail.
//
// Env required (set on the Pages project):
//   PURELYMAIL_API_KEY — Purelymail API token (pm-live-...)

const TO_ADDRESS = "hello@statelyshades.com";
const FROM_ADDRESS = "hello@statelyshades.com";
const FROM_NAME = "Stately Shades Website";

export async function onRequestPost({ request, env }) {
  if (!env.PURELYMAIL_API_KEY) {
    return json({ error: "Mail service is not configured." }, 500);
  }

  let data;
  try {
    const ct = request.headers.get("content-type") || "";
    if (ct.includes("application/json")) {
      data = await request.json();
    } else {
      // Fallback: form-encoded (lets the form work even without JS)
      const fd = await request.formData();
      data = Object.fromEntries(fd.entries());
    }
  } catch (_) {
    return json({ error: "Could not read the request." }, 400);
  }

  const name = (data.name || "").toString().trim();
  const phone = (data.phone || "").toString().trim();
  const email = (data.email || "").toString().trim();
  const location = (data.location || "").toString().trim();
  const interest = (data.interest || "").toString().trim();
  const message = (data.message || "").toString().trim();
  const source = (data.source || "unknown").toString().trim().slice(0, 32);

  if (!name || !phone || !email) {
    return json({ error: "Name, phone, and email are required." }, 400);
  }
  if (!/^\S+@\S+\.\S+$/.test(email)) {
    return json({ error: "That email address looks invalid." }, 400);
  }

  const subject = `New consultation request — ${name}`;

  const textBody =
`New free consultation request from the Stately Shades website.

Source form: ${source}

Name:        ${name}
Phone:       ${phone}
Email:       ${email}
City / ZIP:  ${location || "(not provided)"}
Considering: ${interest || "(not specified)"}

Message:
${message || "(no message)"}

View this lead in the CRM:
https://statelyshades.com/crm/
`;

  const htmlBody = `
<div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; color: #14110D; max-width: 600px; line-height: 1.55;">
  <h2 style="font-family: 'Cormorant Garamond', Georgia, serif; font-weight: 400; font-size: 26px; margin: 0 0 8px;">New consultation request</h2>
  <p style="margin: 0 0 20px; font-family: ui-monospace, 'SF Mono', Menlo, monospace; font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; color: #9D7A3E;">Source: ${esc(source)} form</p>
  <table style="border-collapse: collapse; width: 100%; margin: 0 0 24px;">
    <tr><td style="padding: 8px 12px 8px 0; color: #56493C; width: 130px;">Name</td><td style="padding: 8px 0;"><strong>${esc(name)}</strong></td></tr>
    <tr><td style="padding: 8px 12px 8px 0; color: #56493C;">Phone</td><td style="padding: 8px 0;"><a href="tel:${esc(phone)}" style="color: #9D7A3E;">${esc(phone)}</a></td></tr>
    <tr><td style="padding: 8px 12px 8px 0; color: #56493C;">Email</td><td style="padding: 8px 0;"><a href="mailto:${esc(email)}" style="color: #9D7A3E;">${esc(email)}</a></td></tr>
    <tr><td style="padding: 8px 12px 8px 0; color: #56493C;">City / ZIP</td><td style="padding: 8px 0;">${esc(location || "(not provided)")}</td></tr>
    <tr><td style="padding: 8px 12px 8px 0; color: #56493C;">Considering</td><td style="padding: 8px 0;">${esc(interest || "(not specified)")}</td></tr>
  </table>
  <p style="margin: 0 0 8px; color: #56493C;">Message:</p>
  <div style="background: #F7F2EA; border-left: 2px solid #9D7A3E; padding: 14px 18px; white-space: pre-wrap;">${esc(message || "(no message)")}</div>
  <p style="margin: 28px 0 0;"><a href="https://statelyshades.com/crm/" style="display: inline-block; padding: 10px 18px; background: #14110D; color: #F7F2EA; text-decoration: none; font-family: ui-monospace, 'SF Mono', Menlo, monospace; font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase; border-radius: 2px;">Open in CRM →</a></p>
  <p style="margin: 28px 0 0; font-size: 12px; color: #8B7F6F;">Sent from the Stately Shades website. This lead has been saved to the CRM automatically.</p>
</div>`;

  const purelyResp = await fetch("https://purelymail.com/api/v0/sendMail", {
    method: "POST",
    headers: {
      "Purelymail-Api-Token": env.PURELYMAIL_API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      name: FROM_NAME,
      from: FROM_ADDRESS,
      to: [TO_ADDRESS],
      replyTo: email,
      subject,
      body: textBody,
      bodyHtml: htmlBody,
    }),
  });

  let mailError = null;
  if (!purelyResp.ok) {
    const errText = await purelyResp.text().catch(() => "");
    console.error("Purelymail send failed:", purelyResp.status, errText);
    mailError = "purelymail_http_" + purelyResp.status;
  } else {
    let payload = null;
    try { payload = await purelyResp.json(); } catch (_) {}
    if (payload && payload.type && payload.type !== "success") {
      console.error("Purelymail returned non-success:", payload);
      mailError = "purelymail_" + (payload.type || "unknown");
    }
  }

  // Persist lead to D1 (CRM) regardless of mail outcome
  if (env.DB) {
    try {
      const ipRaw = request.headers.get("CF-Connecting-IP") || "";
      const ipHash = ipRaw ? await sha256B64Trunc(ipRaw, 22) : null;
      const ua = (request.headers.get("user-agent") || "").slice(0, 240);
      const ref = (request.headers.get("referer") || "").slice(0, 500) || null;
      const urlObj = new URL(request.url);
      const utm_source = urlObj.searchParams.get("utm_source");
      const utm_medium = urlObj.searchParams.get("utm_medium");
      const utm_campaign = urlObj.searchParams.get("utm_campaign");
      const utm_term = urlObj.searchParams.get("utm_term");
      const utm_content = urlObj.searchParams.get("utm_content");

      await env.DB.prepare(
        `INSERT INTO leads
          (name, phone, email, location, interest, message,
           source_page, utm_source, utm_medium, utm_campaign, utm_term, utm_content,
           referrer, user_agent, ip_hash)
         VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10, ?11, ?12, ?13, ?14, ?15)`
      )
        .bind(
          name, phone, email, location || null, interest || null, message || null,
          source,
          utm_source, utm_medium, utm_campaign, utm_term, utm_content,
          ref, ua, ipHash
        )
        .run();
    } catch (e) {
      console.error("D1 lead insert failed:", e.message);
      // don't fail the user request just because CRM write failed
    }
  }

  if (mailError) {
    return json(
      { error: "We couldn't send your request right now. Please call us at 629-298-8241." },
      502
    );
  }
  return json({ success: true }, 200);
}

async function sha256B64Trunc(s, n) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  let str = "";
  const bytes = new Uint8Array(buf);
  for (let i = 0; i < bytes.length; i++) str += String.fromCharCode(bytes[i]);
  return btoa(str).slice(0, n);
}

// CORS / non-POST handler — small but polite
export async function onRequest({ request }) {
  if (request.method === "POST") {
    // Should never reach here; onRequestPost takes precedence.
    return new Response("Method handled separately", { status: 200 });
  }
  return json({ error: "Method not allowed." }, 405);
}

function json(body, status) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "Content-Type": "application/json",
      "Cache-Control": "no-store",
    },
  });
}

function esc(s) {
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}
