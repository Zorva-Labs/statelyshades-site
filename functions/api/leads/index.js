import { requireAuth, json } from "../../_lib/auth.js";

const ALLOWED_STATUSES = new Set([
  "new",
  "contacted",
  "quoted",
  "scheduled",
  "installed",
  "won",
  "lost",
  "spam",
]);

export async function onRequestGet(context) {
  const guard = await requireAuth(context);
  if (guard instanceof Response) return guard;

  const url = new URL(context.request.url);
  const status = url.searchParams.get("status");
  const search = (url.searchParams.get("q") || "").trim();
  const limit = Math.min(parseInt(url.searchParams.get("limit") || "200", 10), 500);

  const where = [];
  const binds = [];
  if (status && ALLOWED_STATUSES.has(status)) {
    where.push(`status = ?${binds.length + 1}`);
    binds.push(status);
  }
  if (search) {
    const like = `%${search}%`;
    const i = binds.length + 1;
    where.push(`(name LIKE ?${i} OR email LIKE ?${i + 1} OR phone LIKE ?${i + 2} OR location LIKE ?${i + 3})`);
    binds.push(like, like, like, like);
  }

  const sql = `
    SELECT id, created_at, updated_at, name, phone, email, location, interest,
           message, source_page, status, assigned_to, quoted_amount_cents
    FROM leads
    ${where.length ? `WHERE ${where.join(" AND ")}` : ""}
    ORDER BY datetime(created_at) DESC
    LIMIT ${limit}
  `;
  const stmt = binds.length ? context.env.DB.prepare(sql).bind(...binds) : context.env.DB.prepare(sql);
  const { results } = await stmt.all();

  // Quick counts by status for the sidebar
  const counts = await context.env.DB.prepare(
    `SELECT status, COUNT(*) AS n FROM leads GROUP BY status`
  ).all();
  const byStatus = Object.fromEntries((counts.results || []).map((r) => [r.status, r.n]));

  return json({ leads: results, counts: byStatus });
}
