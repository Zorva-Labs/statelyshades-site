import { requireAuth, json } from "../../../_lib/auth.js";

export async function onRequestGet(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const id = parseInt(context.params.id, 10);
  const project = await context.env.DB
    .prepare(`SELECT p.*, c.name AS contact_name, c.email AS contact_email, c.phone AS contact_phone
              FROM projects p JOIN contacts c ON c.id=p.contact_id WHERE p.id=?1`)
    .bind(id).first();
  if (!project) return json({ error: "Not found" }, 404);
  // Join product info so the print worksheet + windows tab can show product
  // name + retail price without a second round-trip.
  const windows = (await context.env.DB.prepare(
    `SELECT w.*,
            pr.name           AS product_name,
            pr.sku            AS product_sku,
            pr.base_price_cents AS product_price_cents,
            pr.category       AS product_category
       FROM windows w
       LEFT JOIN products pr ON pr.id = w.product_id
      WHERE w.project_id = ?1
      ORDER BY w.position, w.id`
  ).bind(id).all()).results || [];
  const estimates = (await context.env.DB.prepare(`SELECT id, number, status, total_cents, valid_until, created_at FROM estimates WHERE project_id=?1 ORDER BY created_at DESC`).bind(id).all()).results || [];
  const proposals = (await context.env.DB.prepare(`SELECT id, number, status, selected_tier, selected_total_cents, created_at FROM proposals WHERE project_id=?1 ORDER BY created_at DESC`).bind(id).all()).results || [];
  const contracts = (await context.env.DB.prepare(`SELECT id, number, status, total_cents, deposit_cents, deposit_paid, contract_type, view_token, signed_by_customer_at, counter_signed_at, sent_at, created_at FROM contracts WHERE project_id=?1 ORDER BY created_at DESC`).bind(id).all()).results || [];

  // Appointments — directly linked to this project OR matching the contact's
  // email (legacy bookings that pre-date the project_id wiring still attribute
  // via email match). Newest first.
  const appointments = (await context.env.DB.prepare(
    `SELECT id, type, start_at, end_at, duration_min, status, source, name, email, phone, site_address, rooms, notes, created_at
       FROM appointments
      WHERE project_id = ?1
         OR (LOWER(email) = LOWER(?2) AND project_id IS NULL)
      ORDER BY start_at DESC`
  ).bind(id, project.contact_email || "").all()).results || [];

  // Original lead context (interest, message, source, UTM) if this project
  // came from a website inquiry. The lead row stays in D1 even after the
  // job is booked — the Job page is now the surface where it shows up.
  let lead = null;
  let leadNotes = [];
  if (project.lead_id) {
    lead = await context.env.DB.prepare(
      `SELECT id, name, email, phone, interest, message, source_page, utm_source, utm_medium,
              utm_campaign, referrer, created_at, status
         FROM leads WHERE id = ?1`
    ).bind(project.lead_id).first();
    // Admin's hand-typed notes on the lead carry through to the job —
    // the job page surfaces them so nothing the admin captured before
    // contract signing gets lost when the record transitions.
    leadNotes = (await context.env.DB.prepare(
      `SELECT id, body, author, created_at FROM lead_notes WHERE lead_id = ?1 ORDER BY datetime(created_at) DESC`
    ).bind(project.lead_id).all()).results || [];
  }

  // Quick email counts — full thread is on the Messages tab.
  const emailCount = await context.env.DB.prepare(
    `SELECT
       SUM(CASE WHEN direction='out' THEN 1 ELSE 0 END) AS sent,
       SUM(CASE WHEN direction='in'  THEN 1 ELSE 0 END) AS received,
       MAX(created_at) AS last_at
       FROM email_messages WHERE project_id = ?1`
  ).bind(id).first();

  return json({ project, windows, estimates, proposals, contracts, appointments, lead, lead_notes: leadNotes, email_count: emailCount });
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
