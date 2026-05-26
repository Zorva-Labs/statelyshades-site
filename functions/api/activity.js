// GET /api/activity?entity_type=&entity_id=&limit=  — recent activity feed
import { requireAuth, json } from "../_lib/auth.js";

export async function onRequestGet(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const url = new URL(context.request.url);
  const entityType = url.searchParams.get("entity_type");
  const entityId = url.searchParams.get("entity_id");
  const limit = Math.min(parseInt(url.searchParams.get("limit") || "50", 10), 200);

  let sql = `SELECT * FROM activity_log WHERE 1=1`;
  const binds = [];
  if (entityType) { binds.push(entityType); sql += ` AND entity_type = ?${binds.length}`; }
  if (entityId) { binds.push(parseInt(entityId, 10)); sql += ` AND entity_id = ?${binds.length}`; }
  sql += ` ORDER BY created_at DESC LIMIT ${limit}`;
  const rows = (await context.env.DB.prepare(sql).bind(...binds).all()).results || [];
  return json({ activity: rows });
}
