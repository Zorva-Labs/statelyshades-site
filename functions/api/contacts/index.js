import { requireAuth, json } from "../../_lib/auth.js";
import { upsertContact } from "../../_lib/db.js";

export async function onRequestGet(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const url = new URL(context.request.url);
  const q = url.searchParams.get("q");
  let sql = `SELECT * FROM contacts`;
  const binds = [];
  if (q) { sql += ` WHERE name LIKE ?1 OR email LIKE ?1 OR phone LIKE ?1`; binds.push(`%${q}%`); }
  sql += ` ORDER BY updated_at DESC LIMIT 200`;
  const rows = (await context.env.DB.prepare(sql).bind(...binds).all()).results || [];
  return json({ contacts: rows });
}

export async function onRequestPost(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const body = await context.request.json().catch(() => ({}));
  if (!body.name || !body.email) return json({ error: "Missing name or email" }, 400);
  const id = await upsertContact(context.env.DB, {
    name: body.name, email: body.email, phone: body.phone, address: body.address,
  });
  return json({ id });
}
