// POST /api/proposals/[id]/convert — turn an accepted proposal into a draft contract
// (booking flow shortcut — Tave-style "convert to job")
import { requireAuth, json } from "../../../_lib/auth.js";
import { genToken, nextSequence, formatDocNumber } from "../../../_lib/tokens.js";
import { recordActivity } from "../../../_lib/db.js";

const DEFAULT_TERMS = `<h3>Materials &amp; Manufacture</h3>
<p>All custom window treatments listed in this agreement are made-to-order. Manufacturer lead times typically run two to six weeks from order placement.</p>
<h3>Deposit &amp; Payment</h3>
<p>A deposit of fifty percent (50%) of the total contract price is due at signing to release the order. Balance due at completion of installation.</p>
<h3>Cancellation</h3>
<p>Custom orders are non-returnable once released to the manufacturer. Customer may cancel within 72 hours of signing without penalty.</p>
<h3>Warranty</h3>
<p>All products carry the original manufacturer warranty. Installation work is warranted for ninety (90) days against defects in workmanship.</p>`;

export async function onRequestPost(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const proposalId = parseInt(context.params.id, 10);

  const proposal = await context.env.DB
    .prepare(`SELECT * FROM proposals WHERE id = ?1`)
    .bind(proposalId)
    .first();
  if (!proposal) return json({ error: "Proposal not found" }, 404);

  // Determine which tier to use (use selected_tier, else "best")
  const tierKey = proposal.selected_tier || "best";
  const tier = await context.env.DB
    .prepare(`SELECT * FROM proposal_tiers WHERE proposal_id = ?1 AND tier = ?2`)
    .bind(proposalId, tierKey)
    .first();
  if (!tier) return json({ error: "Tier not found on proposal" }, 400);

  // Build the contract
  const year = new Date().getUTCFullYear();
  const seq = await nextSequence(context.env.DB, `contract-${year}`);
  const number = formatDocNumber("C", year, seq);
  const token = genToken(16);
  const totalCents = tier.total_cents || 0;
  const depositCents = Math.round(totalCents / 2);

  const r = await context.env.DB.prepare(
    `INSERT INTO contracts (project_id, proposal_id, number, view_token, status, total_cents, deposit_cents,
       intro, scope_html, terms_html, estimated_install_window, author_user_id)
     VALUES (?1, ?2, ?3, ?4, 'draft', ?5, ?6, ?7, ?8, ?9, ?10, ?11) RETURNING id`
  ).bind(
    proposal.project_id, proposalId, number, token, totalCents, depositCents,
    "This agreement is between Stately Shades (Gallatin, TN) and the customer below for the supply and installation of custom window treatments at the project address listed.",
    `<p>Per the accepted <strong>${tierKey}</strong> tier of proposal ${proposal.number}.</p>`,
    DEFAULT_TERMS,
    "Weeks 4–6 from contract execution",
    auth.id,
  ).first();

  // Copy lines from the chosen tier
  const lines = (await context.env.DB
    .prepare(`SELECT description, room, quantity, unit_price_cents, line_total_cents, position FROM proposal_tier_lines WHERE tier_id = ?1 ORDER BY position, id`)
    .bind(tier.id).all()).results || [];
  for (const l of lines) {
    await context.env.DB.prepare(
      `INSERT INTO contract_lines (contract_id, description, room, quantity, unit_price_cents, line_total_cents, position)
       VALUES (?1,?2,?3,?4,?5,?6,?7)`
    ).bind(r.id, l.description, l.room, l.quantity, l.unit_price_cents, l.line_total_cents, l.position).run();
  }

  // Move project status forward
  await context.env.DB
    .prepare(`UPDATE projects SET status = 'proposed', updated_at = datetime('now') WHERE id = ?1`)
    .bind(proposal.project_id)
    .run();

  await recordActivity(context.env.DB, {
    entityType: "contract", entityId: r.id, action: "created-from-proposal",
    actorKind: "admin", actorId: auth.id, actorName: auth.email,
    details: { proposal_id: proposalId, tier: tierKey, total_cents: totalCents },
  });

  return json({ id: r.id, number, view_token: token });
}
