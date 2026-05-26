// POST /api/leads/[id]/send-proposal
// One-call flow from a lead -> upsert contact -> create project -> create proposal.
// Body: { project_name?, template_id? }
import { requireAuth, json } from "../../../_lib/auth.js";
import { upsertContact, recordActivity } from "../../../_lib/db.js";
import { genToken, nextSequence, formatDocNumber } from "../../../_lib/tokens.js";
import { seedTiersFromWindows } from "../../../_lib/lifecycle.js";

const TIERS = ["good", "better", "best"];

export async function onRequestPost(context) {
  const auth = await requireAuth(context); if (auth instanceof Response) return auth;
  const leadId = parseInt(context.params.id, 10);
  if (!Number.isFinite(leadId)) return json({ error: "Invalid lead id" }, 400);

  const body = await context.request.json().catch(() => ({}));
  const { DB } = context.env;

  const lead = await DB.prepare(`SELECT * FROM leads WHERE id = ?1`).bind(leadId).first();
  if (!lead) return json({ error: "Lead not found" }, 404);
  if (!lead.email) return json({ error: "Lead has no email — add one before sending a proposal" }, 400);

  // 1. Upsert contact from lead data
  const contactId = await upsertContact(DB, {
    name: lead.name,
    email: lead.email,
    phone: lead.phone,
    address: {
      street: lead.address_street,
      city:   lead.address_city,
      state:  lead.address_state,
      zip:    lead.address_zip,
    },
  });

  // 2. Create project — name comes from body or sensibly defaults from lead.interest
  const projectName = (body.project_name && String(body.project_name).trim()) ||
    (lead.interest ? `${lead.interest} — ${lead.name}` : `Whole house — ${lead.name}`);
  const siteAddress = [lead.address_street, [lead.address_city, lead.address_state].filter(Boolean).join(", "), lead.address_zip].filter(Boolean).join(", ") || null;

  const projectRow = await DB.prepare(
    `INSERT INTO projects (contact_id, lead_id, name, description, status, site_address)
     VALUES (?1, ?2, ?3, ?4, 'quoted', ?5) RETURNING id`
  ).bind(contactId, leadId, projectName, lead.message || null, siteAddress).first();
  const projectId = projectRow.id;

  // 3. Create proposal — load default template if no template_id given
  const tpl = body.template_id
    ? await DB.prepare(`SELECT * FROM document_templates WHERE id=?1`).bind(body.template_id).first()
    : await DB.prepare(`SELECT * FROM document_templates WHERE kind='proposal' AND is_default=1 ORDER BY id LIMIT 1`).first();
  const intro = tpl?.intro || "Thank you for the opportunity to dress your windows. We've put together three options below — each one custom-fit to your home.";
  const tierTitles = {
    good:   tpl?.tier_good_title   || "The Essentials",
    better: tpl?.tier_better_title || "The Smart-Home Package",
    best:   tpl?.tier_best_title   || "The Heirloom Build",
  };

  const year = new Date().getUTCFullYear();
  const seq = await nextSequence(DB, `proposal-${year}`);
  const number = formatDocNumber("PROP", year, seq);
  const token = genToken(16);
  const validUntil = new Date(Date.now() + 30 * 86400 * 1000).toISOString().slice(0, 10);

  const proposalRow = await DB.prepare(
    `INSERT INTO proposals (project_id, number, view_token, status, intro, valid_until, author_user_id)
     VALUES (?1, ?2, ?3, 'draft', ?4, ?5, ?6) RETURNING id`
  ).bind(projectId, number, token, intro, validUntil, auth.id).first();

  for (const t of TIERS) {
    await DB.prepare(`INSERT INTO proposal_tiers (proposal_id, tier, title) VALUES (?1, ?2, ?3)`).bind(proposalRow.id, t, tierTitles[t]).run();
  }
  // Pre-populate each tier from the windows the admin already entered on the lead
  await seedTiersFromWindows(DB, proposalRow.id, projectId);

  // 4. Update lead: link to the new contact + bump status to 'quoted'
  await DB.prepare(
    `UPDATE leads SET contact_id = ?1, status = 'quoted', updated_at = datetime('now') WHERE id = ?2`
  ).bind(contactId, leadId).run();

  // 5. Audit
  await recordActivity(DB, {
    entityType: "lead", entityId: leadId, action: "proposal-started",
    actorKind: "admin", actorId: auth.id, actorName: auth.email,
    details: { contact_id: contactId, project_id: projectId, proposal_id: proposalRow.id, proposal_number: number },
  });
  await recordActivity(DB, {
    entityType: "proposal", entityId: proposalRow.id, action: "created-from-lead",
    actorKind: "admin", actorId: auth.id, actorName: auth.email,
    details: { lead_id: leadId },
  });

  return json({
    contact_id: contactId,
    project_id: projectId,
    proposal_id: proposalRow.id,
    proposal_number: number,
    view_token: token,
  });
}
