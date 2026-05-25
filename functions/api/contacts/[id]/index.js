import { requireAuth, json } from "../../../_lib/auth.js";

export async function onRequestGet(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const id = parseInt(context.params.id, 10);
  const c = await context.env.DB.prepare(`SELECT * FROM contacts WHERE id = ?1`).bind(id).first();
  if (!c) return json({ error: "Not found" }, 404);
  const projects = (await context.env.DB.prepare(`SELECT * FROM projects WHERE contact_id = ?1 ORDER BY created_at DESC`).bind(id).all()).results || [];
  const appointments = (await context.env.DB.prepare(`SELECT * FROM appointments WHERE contact_id = ?1 ORDER BY start_at DESC LIMIT 50`).bind(id).all()).results || [];
  return json({ contact: c, projects, appointments });
}

export async function onRequestPatch(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const id = parseInt(context.params.id, 10);
  const body = await context.request.json().catch(() => ({}));
  const fields = [];
  const binds = [];
  const allowed = ["name","email","phone","address_street","address_city","address_state","address_zip","notes"];
  for (const k of allowed) {
    if (body[k] !== undefined) { fields.push(`${k}=?${binds.length+1}`); binds.push(body[k]); }
  }
  if (!fields.length) return json({ error: "Nothing to update" }, 400);
  fields.push(`updated_at=datetime('now')`);
  binds.push(id);
  await context.env.DB.prepare(`UPDATE contacts SET ${fields.join(", ")} WHERE id=?${binds.length}`).bind(...binds).run();
  return json({ ok: true });
}
