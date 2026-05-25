// GET /api/public/proposal/[token]  → proposal + tiers + lines + comments
// POST /api/public/proposal/[token]  body: { action: "select_tier" | "accept" | "comment", tier?, name?, body? }
import { json, hashIp } from "../../../_lib/auth.js";
import { trackView, recordActivity } from "../../../_lib/db.js";

export async function onRequestGet(context) {
  const token = context.params.token;
  const p = await context.env.DB.prepare(
    `SELECT pr.*, pj.name AS project_name, c.name AS contact_name
     FROM proposals pr JOIN projects pj ON pj.id=pr.project_id JOIN contacts c ON c.id=pj.contact_id
     WHERE pr.view_token=?1`
  ).bind(token).first();
  if (!p) return json({ error: "Not found" }, 404);
  const tiers = (await context.env.DB.prepare(`SELECT * FROM proposal_tiers WHERE proposal_id=?1 ORDER BY CASE tier WHEN 'good' THEN 1 WHEN 'better' THEN 2 WHEN 'best' THEN 3 END`).bind(p.id).all()).results || [];
  for (const t of tiers) {
    t.lines = (await context.env.DB.prepare(`SELECT * FROM proposal_tier_lines WHERE tier_id=?1 ORDER BY position, id`).bind(t.id).all()).results || [];
  }
  const comments = (await context.env.DB.prepare(`SELECT id, tier, author_kind, author_name, body, created_at FROM proposal_comments WHERE proposal_id=?1 ORDER BY created_at ASC`).bind(p.id).all()).results || [];
  await trackView(context.env.DB, "proposals", p.id);
  if (p.status === "sent") await context.env.DB.prepare(`UPDATE proposals SET status='viewed' WHERE id=?1`).bind(p.id).run();
  const safe = { ...p }; delete safe.notes_internal; delete safe.author_user_id;
  return json({ proposal: safe, tiers, comments });
}

export async function onRequestPost(context) {
  const token = context.params.token;
  const body = await context.request.json().catch(() => ({}));
  const p = await context.env.DB.prepare(`SELECT * FROM proposals WHERE view_token=?1`).bind(token).first();
  if (!p) return json({ error: "Not found" }, 404);
  const ipHash = await hashIp(context.request.headers.get("CF-Connecting-IP"));

  if (body.action === "select_tier") {
    if (!["good","better","best"].includes(body.tier)) return json({ error: "Invalid tier" }, 400);
    const t = await context.env.DB.prepare(`SELECT total_cents FROM proposal_tiers WHERE proposal_id=?1 AND tier=?2`).bind(p.id, body.tier).first();
    await context.env.DB.prepare(
      `UPDATE proposals SET selected_tier=?1, selected_total_cents=?2, status='tier_selected', updated_at=datetime('now') WHERE id=?3`
    ).bind(body.tier, t?.total_cents || 0, p.id).run();
    await recordActivity(context.env.DB, {
      entityType: "proposal", entityId: p.id, action: "tier-selected",
      actorKind: "customer", details: { tier: body.tier, ip_hash: ipHash },
    });
    return json({ ok: true });
  }

  if (body.action === "accept") {
    if (!body.name) return json({ error: "Please type your name to accept." }, 400);
    if (!p.selected_tier) return json({ error: "Pick a tier first." }, 400);
    await context.env.DB.prepare(
      `UPDATE proposals SET status='accepted', accepted_at=datetime('now'), accepted_by_name=?1, accepted_ip_hash=?2, updated_at=datetime('now') WHERE id=?3`
    ).bind(body.name, ipHash, p.id).run();
    await recordActivity(context.env.DB, {
      entityType: "proposal", entityId: p.id, action: "accepted",
      actorKind: "customer", actorName: body.name,
      details: { ip_hash: ipHash, tier: p.selected_tier },
    });
    return json({ ok: true });
  }

  if (body.action === "comment") {
    if (!body.body) return json({ error: "Empty comment" }, 400);
    await context.env.DB.prepare(
      `INSERT INTO proposal_comments (proposal_id, tier, author_kind, author_name, body)
       VALUES (?1, ?2, 'customer', ?3, ?4)`
    ).bind(p.id, body.tier || null, body.name || null, body.body).run();
    await recordActivity(context.env.DB, {
      entityType: "proposal", entityId: p.id, action: "comment-added",
      actorKind: "customer", actorName: body.name || null,
    });
    return json({ ok: true });
  }

  return json({ error: "Unknown action" }, 400);
}
