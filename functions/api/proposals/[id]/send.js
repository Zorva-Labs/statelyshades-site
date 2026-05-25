import { requireAuth, json } from "../../../_lib/auth.js";
import { sendEmail, brandedEmail, escapeHtml } from "../../../_lib/email.js";
import { recordActivity } from "../../../_lib/db.js";

const SITE_URL = "https://statelyshades.com";

export async function onRequestPost(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const id = parseInt(context.params.id, 10);
  const p = await context.env.DB.prepare(
    `SELECT pr.*, pj.name AS project_name, c.name AS contact_name, c.email AS contact_email
     FROM proposals pr JOIN projects pj ON pj.id=pr.project_id JOIN contacts c ON c.id=pj.contact_id
     WHERE pr.id=?1`
  ).bind(id).first();
  if (!p) return json({ error: "Not found" }, 404);
  const url = `${SITE_URL}/proposal/?t=${p.view_token}`;
  await sendEmail(context.env, {
    to: p.contact_email,
    subject: `Your proposal — ${p.number}`,
    html: brandedEmail({
      title: "Your proposal is ready to review.",
      body: `
        <p>Hi ${escapeHtml(p.contact_name.split(" ")[0])},</p>
        <p>Here's the proposal for <strong>${escapeHtml(p.project_name)}</strong>. We've laid out three options — pick the one that fits, or write back with questions.</p>
        ${p.intro ? `<p style="border-left:3px solid #9D7A3E;padding-left:14px;color:#56493C;font-style:italic">${escapeHtml(p.intro)}</p>` : ""}
        <p>Open the proposal online to compare tiers side-by-side.</p>
      `,
      ctaLabel: "Open Your Proposal",
      ctaUrl: url,
    }),
    text: `Your proposal ${p.number} is ready: ${url}`,
  });
  await context.env.DB.prepare(
    `UPDATE proposals SET status='sent', sent_at=datetime('now'), updated_at=datetime('now') WHERE id=?1`
  ).bind(id).run();
  await recordActivity(context.env.DB, {
    entityType: "proposal", entityId: id, action: "sent",
    actorKind: "admin", actorId: auth.id, actorName: auth.email,
  });
  return json({ ok: true, url });
}
