import { requireAuth, json } from "../../../_lib/auth.js";

export async function onRequestGet(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const id = parseInt(context.params.id, 10);
  const project = await context.env.DB
    .prepare(`SELECT p.*, c.name AS contact_name, c.email AS contact_email, c.phone AS contact_phone
              FROM projects p JOIN contacts c ON c.id=p.contact_id WHERE p.id=?1`)
    .bind(id).first();
  if (!project) return json({ error: "Not found" }, 404);
  const windows = (await context.env.DB.prepare(`SELECT * FROM windows WHERE project_id=?1 ORDER BY position, id`).bind(id).all()).results || [];
  const estimates = (await context.env.DB.prepare(`SELECT id, number, status, total_cents, valid_until, created_at FROM estimates WHERE project_id=?1 ORDER BY created_at DESC`).bind(id).all()).results || [];
  const proposals = (await context.env.DB.prepare(`SELECT id, number, status, selected_tier, selected_total_cents, created_at FROM proposals WHERE project_id=?1 ORDER BY created_at DESC`).bind(id).all()).results || [];
  const contracts = (await context.env.DB.prepare(`SELECT id, number, status, total_cents, deposit_cents, deposit_paid, created_at FROM contracts WHERE project_id=?1 ORDER BY created_at DESC`).bind(id).all()).results || [];
  return json({ project, windows, estimates, proposals, contracts });
}

export async function onRequestPatch(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const id = parseInt(context.params.id, 10);
  const body = await context.request.json().catch(() => ({}));
  const fields = [];
  const binds = [];
  const allowed = ["name","description","site_address","status"];
  for (const k of allowed) {
    if (body[k] !== undefined) { fields.push(`${k}=?${binds.length+1}`); binds.push(body[k]); }
  }
  if (!fields.length) return json({ error: "Nothing to update" }, 400);
  fields.push(`updated_at=datetime('now')`);
  binds.push(id);
  await context.env.DB.prepare(`UPDATE projects SET ${fields.join(", ")} WHERE id=?${binds.length}`).bind(...binds).run();
  return json({ ok: true });
}

export async function onRequestDelete(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const id = parseInt(context.params.id, 10);
  await context.env.DB.prepare(`DELETE FROM projects WHERE id=?1`).bind(id).run();
  return json({ ok: true });
}
