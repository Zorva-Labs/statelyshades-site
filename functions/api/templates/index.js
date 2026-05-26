import { requireAuth, json } from "../../_lib/auth.js";

export async function onRequestGet(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const url = new URL(context.request.url);
  const category = url.searchParams.get("category");
  let sql = `SELECT * FROM email_templates WHERE active = 1`;
  const binds = [];
  if (category) { binds.push(category); sql += ` AND category = ?${binds.length}`; }
  sql += ` ORDER BY category, name`;
  const rows = (await context.env.DB.prepare(sql).bind(...binds).all()).results || [];
  return json({ templates: rows });
}

export async function onRequestPost(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const body = await context.request.json().catch(() => ({}));
  if (!body.slug || !body.name || !body.subject || !body.body_html) {
    return json({ error: "Missing slug, name, subject, or body_html" }, 400);
  }
  const r = await context.env.DB.prepare(
    `INSERT INTO email_templates (slug, name, category, subject, body_html, body_text, description)
     VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7) RETURNING id`
  ).bind(body.slug, body.name, body.category || "general", body.subject, body.body_html, body.body_text || null, body.description || null).first();
  return json({ id: r.id });
}
