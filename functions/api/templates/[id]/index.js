import { requireAuth, json } from "../../../_lib/auth.js";

export async function onRequestGet(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const id = parseInt(context.params.id, 10);
  const t = await context.env.DB.prepare(`SELECT * FROM email_templates WHERE id = ?1`).bind(id).first();
  if (!t) return json({ error: "Not found" }, 404);
  return json({ template: t });
}

export async function onRequestPatch(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const id = parseInt(context.params.id, 10);
  const body = await context.request.json().catch(() => ({}));
  const allowed = ["name", "category", "subject", "body_html", "body_text", "description", "active"];
  const fields = []; const binds = [];
  for (const k of allowed) {
    if (body[k] !== undefined) { fields.push(`${k}=?${binds.length+1}`); binds.push(typeof body[k] === "boolean" ? (body[k] ? 1 : 0) : body[k]); }
  }
  if (!fields.length) return json({ error: "Nothing to update" }, 400);
  fields.push(`updated_at=datetime('now')`);
  binds.push(id);
  await context.env.DB.prepare(`UPDATE email_templates SET ${fields.join(", ")} WHERE id=?${binds.length}`).bind(...binds).run();
  return json({ ok: true });
}

export async function onRequestDelete(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  await context.env.DB.prepare(`UPDATE email_templates SET active=0 WHERE id=?1`).bind(parseInt(context.params.id, 10)).run();
  return json({ ok: true });
}
