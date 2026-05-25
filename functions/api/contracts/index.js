import { requireAuth, json } from "../../_lib/auth.js";
import { genToken, nextSequence, formatDocNumber } from "../../_lib/tokens.js";
import { recordActivity } from "../../_lib/db.js";

const DEFAULT_TERMS = `
<h3>Materials &amp; Manufacture</h3>
<p>All custom window treatments listed in this agreement are made-to-order. Manufacturer lead times typically run two to six weeks from order placement. We will keep you informed of any changes to the schedule.</p>

<h3>Deposit &amp; Payment</h3>
<p>A deposit of fifty percent (50%) of the total contract price is due at signing to release the order to our manufacturing partners. The balance is due at the completion of installation. We accept check, cash, ACH, Venmo, and Cash App. Card payments incur a 3% convenience fee.</p>

<h3>Measurement &amp; Fit</h3>
<p>Stately Shades will measure all windows on-site and is responsible for the fit of any product we manufacture from those measurements. For install-only service (customer-supplied products), the customer is responsible for the correctness of dimensions ordered.</p>

<h3>Cancellation</h3>
<p>Custom orders are non-returnable once released to the manufacturer. The customer may cancel within 72 hours of signing without penalty. After 72 hours, the deposit is non-refundable to the extent it covers materials already ordered. Stately Shades reserves the right to cancel and refund the deposit if the project becomes unworkable.</p>

<h3>Warranty</h3>
<p>All products carry the original manufacturer warranty (typically 5–25 years depending on product line). Our installation work is warranted for ninety (90) days against defects in workmanship — we will return and repair at no charge for any install defect reported within that window.</p>

<h3>Site Access &amp; Conditions</h3>
<p>The customer is responsible for providing reasonable site access at the scheduled install time and a working environment safe for our installers (clear paths to windows, pets contained, hazards disclosed). Postponements due to inaccessible sites may incur a re-scheduling fee.</p>

<h3>Photography</h3>
<p>Stately Shades may photograph completed installations for portfolio and marketing use. Customers who prefer not to have their home photographed should note this here or notify us before install day.</p>
`;

export async function onRequestGet(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const url = new URL(context.request.url);
  const status = url.searchParams.get("status");
  const projectId = url.searchParams.get("project_id");
  let sql = `SELECT k.*, p.name AS project_name, c.name AS contact_name, c.email AS contact_email
             FROM contracts k
             JOIN projects p ON p.id = k.project_id
             JOIN contacts c ON c.id = p.contact_id WHERE 1=1`;
  const binds = [];
  if (status) { binds.push(status); sql += ` AND k.status=?${binds.length}`; }
  if (projectId) { binds.push(parseInt(projectId, 10)); sql += ` AND k.project_id=?${binds.length}`; }
  sql += ` ORDER BY k.created_at DESC LIMIT 200`;
  const rows = (await context.env.DB.prepare(sql).bind(...binds).all()).results || [];
  return json({ contracts: rows });
}

export async function onRequestPost(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const body = await context.request.json().catch(() => ({}));
  if (!body.project_id) return json({ error: "Missing project_id" }, 400);
  const year = new Date().getUTCFullYear();
  const seq = await nextSequence(context.env.DB, `contract-${year}`);
  const number = formatDocNumber("C", year, seq);
  const token = genToken(16);

  // Optionally seed lines from an estimate or proposal tier
  let totalCents = 0;
  let lines = [];
  if (body.estimate_id) {
    const est = await context.env.DB.prepare(`SELECT total_cents FROM estimates WHERE id=?1`).bind(body.estimate_id).first();
    if (est) totalCents = est.total_cents;
    lines = (await context.env.DB.prepare(`SELECT description, room, quantity, unit_price_cents, line_total_cents, position FROM estimate_lines WHERE estimate_id=?1 ORDER BY position, id`).bind(body.estimate_id).all()).results || [];
  } else if (body.proposal_tier_id) {
    const t = await context.env.DB.prepare(`SELECT proposal_id, tier, total_cents FROM proposal_tiers WHERE id=?1`).bind(body.proposal_tier_id).first();
    if (t) {
      totalCents = t.total_cents;
      lines = (await context.env.DB.prepare(`SELECT description, room, quantity, unit_price_cents, line_total_cents, position FROM proposal_tier_lines WHERE tier_id=?1 ORDER BY position, id`).bind(body.proposal_tier_id).all()).results || [];
    }
  }

  const depositCents = body.deposit_cents != null ? parseInt(body.deposit_cents, 10) : Math.round(totalCents / 2);

  const r = await context.env.DB.prepare(
    `INSERT INTO contracts (project_id, estimate_id, proposal_id, number, view_token, status, total_cents, deposit_cents,
       intro, scope_html, terms_html, estimated_install_window, author_user_id)
     VALUES (?1,?2,?3,?4,?5,'draft',?6,?7,?8,?9,?10,?11,?12) RETURNING id`
  ).bind(
    body.project_id,
    body.estimate_id || null,
    body.proposal_id || null,
    number, token, totalCents, depositCents,
    body.intro || "This agreement is between Stately Shades (Gallatin, TN) and the customer below for the supply and installation of custom window treatments at the project address listed.",
    body.scope_html || "",
    body.terms_html || DEFAULT_TERMS,
    body.estimated_install_window || "Weeks 4–6 from contract execution",
    auth.id,
  ).first();

  for (const l of lines) {
    await context.env.DB.prepare(
      `INSERT INTO contract_lines (contract_id, description, room, quantity, unit_price_cents, line_total_cents, position)
       VALUES (?1,?2,?3,?4,?5,?6,?7)`
    ).bind(r.id, l.description, l.room || null, l.quantity, l.unit_price_cents, l.line_total_cents, l.position).run();
  }

  await recordActivity(context.env.DB, {
    entityType: "contract", entityId: r.id, action: "created",
    actorKind: "admin", actorId: auth.id, actorName: auth.email,
  });
  return json({ id: r.id, number, view_token: token });
}
