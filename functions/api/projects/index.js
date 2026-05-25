import { requireAuth, json } from "../../_lib/auth.js";

export async function onRequestGet(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const url = new URL(context.request.url);
  const status = url.searchParams.get("status");
  const contactId = url.searchParams.get("contact_id");
  let sql = `SELECT p.*, c.name AS contact_name, c.email AS contact_email
             FROM projects p JOIN contacts c ON c.id = p.contact_id WHERE 1=1`;
  const binds = [];
  if (status) { binds.push(status); sql += ` AND p.status=?${binds.length}`; }
  if (contactId) { binds.push(parseInt(contactId, 10)); sql += ` AND p.contact_id=?${binds.length}`; }
  sql += ` ORDER BY p.updated_at DESC LIMIT 200`;
  const rows = (await context.env.DB.prepare(sql).bind(...binds).all()).results || [];
  return json({ projects: rows });
}

export async function onRequestPost(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const body = await context.request.json().catch(() => ({}));
  if (!body.contact_id || !body.name) return json({ error: "Missing contact_id or name" }, 400);
  const r = await context.env.DB
    .prepare(`INSERT INTO projects (contact_id, name, description, site_address)
              VALUES (?1,?2,?3,?4) RETURNING id`)
    .bind(body.contact_id, body.name, body.description || null, body.site_address || null)
    .first();
  return json({ id: r.id });
}
