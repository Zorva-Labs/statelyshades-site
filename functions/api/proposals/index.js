import { requireAuth, json } from "../../_lib/auth.js";
import { genToken, nextSequence, formatDocNumber } from "../../_lib/tokens.js";
import { recordActivity } from "../../_lib/db.js";

const TIERS = ["good", "better", "best"];

export async function onRequestGet(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const url = new URL(context.request.url);
  const status = url.searchParams.get("status");
  const projectId = url.searchParams.get("project_id");
  let sql = `SELECT pr.*, p.name AS project_name, c.name AS contact_name, c.email AS contact_email
             FROM proposals pr
             JOIN projects p ON p.id = pr.project_id
             JOIN contacts c ON c.id = p.contact_id WHERE 1=1`;
  const binds = [];
  if (status) { binds.push(status); sql += ` AND pr.status=?${binds.length}`; }
  if (projectId) { binds.push(parseInt(projectId, 10)); sql += ` AND pr.project_id=?${binds.length}`; }
  sql += ` ORDER BY pr.created_at DESC LIMIT 200`;
  const rows = (await context.env.DB.prepare(sql).bind(...binds).all()).results || [];
  return json({ proposals: rows });
}

export async function onRequestPost(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const body = await context.request.json().catch(() => ({}));
  if (!body.project_id) return json({ error: "Missing project_id" }, 400);
  const year = new Date().getUTCFullYear();
  const seq = await nextSequence(context.env.DB, `proposal-${year}`);
  const number = formatDocNumber("PROP", year, seq);
  const token = genToken(16);
  const validDays = parseInt(body.valid_days || 30, 10);
  const validUntil = new Date(Date.now() + validDays * 86400 * 1000).toISOString().slice(0, 10);
  const r = await context.env.DB.prepare(
    `INSERT INTO proposals (project_id, number, view_token, status, intro, notes_internal, valid_until, author_user_id)
     VALUES (?1,?2,?3,'draft',?4,?5,?6,?7) RETURNING id`
  ).bind(
    body.project_id, number, token,
    body.intro || "Thank you for the opportunity to dress your windows. We've put together three options below — each one custom-fit to your home.",
    body.notes_internal || null, validUntil, auth.id,
  ).first();

  // Seed the three tiers
  for (const t of TIERS) {
    await context.env.DB.prepare(
      `INSERT INTO proposal_tiers (proposal_id, tier, title) VALUES (?1,?2,?3)`
    ).bind(r.id, t, defaultTitle(t)).run();
  }
  await recordActivity(context.env.DB, {
    entityType: "proposal", entityId: r.id, action: "created",
    actorKind: "admin", actorId: auth.id, actorName: auth.email,
  });
  return json({ id: r.id, number, view_token: token });
}

function defaultTitle(t) {
  return { good: "The Essentials", better: "The Smart-Home Package", best: "The Heirloom Build" }[t];
}
