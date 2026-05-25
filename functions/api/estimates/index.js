import { requireAuth, json } from "../../_lib/auth.js";
import { genToken, nextSequence, formatDocNumber } from "../../_lib/tokens.js";
import { recordActivity } from "../../_lib/db.js";

export async function onRequestGet(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const url = new URL(context.request.url);
  const status = url.searchParams.get("status");
  const projectId = url.searchParams.get("project_id");
  let sql = `SELECT e.*, p.name AS project_name, c.name AS contact_name, c.email AS contact_email
             FROM estimates e
             JOIN projects p ON p.id = e.project_id
             JOIN contacts c ON c.id = p.contact_id
             WHERE 1=1`;
  const binds = [];
  if (status) { binds.push(status); sql += ` AND e.status=?${binds.length}`; }
  if (projectId) { binds.push(parseInt(projectId, 10)); sql += ` AND e.project_id=?${binds.length}`; }
  sql += ` ORDER BY e.created_at DESC LIMIT 200`;
  const rows = (await context.env.DB.prepare(sql).bind(...binds).all()).results || [];
  return json({ estimates: rows });
}

export async function onRequestPost(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const body = await context.request.json().catch(() => ({}));
  if (!body.project_id) return json({ error: "Missing project_id" }, 400);
  const year = new Date().getUTCFullYear();
  const seq = await nextSequence(context.env.DB, `estimate-${year}`);
  const number = formatDocNumber("EST", year, seq);
  const token = genToken(16);
  const validDays = parseInt(body.valid_days || 30, 10);
  const validUntil = new Date(Date.now() + validDays * 86400 * 1000).toISOString().slice(0, 10);
  const r = await context.env.DB.prepare(
    `INSERT INTO estimates (project_id, number, view_token, status, valid_until, notes_customer, notes_internal, author_user_id)
     VALUES (?1,?2,?3,'draft',?4,?5,?6,?7) RETURNING id`
  ).bind(
    body.project_id, number, token, validUntil,
    body.notes_customer || null, body.notes_internal || null, auth.id,
  ).first();
  await recordActivity(context.env.DB, {
    entityType: "estimate", entityId: r.id, action: "created",
    actorKind: "admin", actorId: auth.id, actorName: auth.email,
  });
  return json({ id: r.id, number, view_token: token });
}
