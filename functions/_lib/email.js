// Purelymail wrapper + branded HTML email templates.
// Env vars used:
//   PURELYMAIL_API_KEY  — bearer token
//   PURELYMAIL_FROM     — defaults to hello@statelyshades.com
//   PURELYMAIL_FROM_NAME — defaults to "Stately Shades"

const PURELYMAIL_ENDPOINT = "https://purelymail.com/api/v0/sendMail";

// Best-effort mail send. Callers `await sendEmail(...)` but we never throw —
// every code path here resolves so a downstream API never crashes because the
// mail provider is unreachable or rejecting. The return shape is informational
// only: { skipped, status, json, error } — most callers ignore it.
export async function sendEmail(env, { to, subject, html, text, replyTo, attachments }) {
  if (!env.PURELYMAIL_API_KEY) {
    console.warn("[email] PURELYMAIL_API_KEY missing — skipping send");
    return { skipped: true, reason: "no_api_key" };
  }
  const from = env.PURELYMAIL_FROM || "hello@statelyshades.com";
  const fromName = env.PURELYMAIL_FROM_NAME || "Stately Shades";
  const body = {
    name: fromName,
    from,
    to: Array.isArray(to) ? to : [to],
    subject,
    body: html || text,
    bodyHtml: html,
    bodyText: text || stripHtml(html),
    replyTo: replyTo || from,
  };
  if (attachments && attachments.length) body.attachments = attachments;

  try {
    const res = await fetch(PURELYMAIL_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        // Purelymail uses a custom header rather than Authorization: Bearer.
        // See ~/.claude/projects/.../memory/reference_purelymail.md.
        "Purelymail-Api-Token": env.PURELYMAIL_API_KEY,
      },
      body: JSON.stringify(body),
    });
    const raw = await res.text().catch(() => "");
    let json;
    try { json = JSON.parse(raw); } catch { json = { raw: raw.slice(0, 200) }; }
    if (!res.ok) {
      console.error("[email] Purelymail send failed:", res.status, raw.slice(0, 200));
    } else if (json && json.type && json.type !== "success") {
      console.error("[email] Purelymail non-success:", json);
    }
    return { status: res.status, json };
  } catch (e) {
    console.error("[email] fetch threw:", e?.message || e);
    return { skipped: true, error: e?.message || "fetch_failed" };
  }
}

function stripHtml(html) {
  if (!html) return "";
  return html.replace(/<[^>]+>/g, "").replace(/\s+/g, " ").trim();
}

// --------------------------------------------------------------
// Shared branded HTML shell
// --------------------------------------------------------------
const BRAND = {
  espresso: "#14110D",
  bg: "#F7F2EA",
  bg2: "#EFE8DB",
  brass: "#9D7A3E",
  champagne: "#D4B896",
  ink: "#14110D",
  inkSoft: "#56493C",
  line: "#D9CFBB",
};

export function brandedEmail({ title, preheader, body, ctaLabel, ctaUrl, footer }) {
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>${escapeHtml(title)}</title>
<style>
  body { margin:0; padding:0; background:${BRAND.bg}; font-family: 'Helvetica Neue', Arial, sans-serif; color:${BRAND.ink}; }
  .wrap { max-width:600px; margin:0 auto; padding:32px 20px; }
  .card { background:#fff; border:1px solid ${BRAND.line}; border-top:3px solid ${BRAND.brass}; padding:36px 32px; }
  .brand { font-family: Georgia, 'Times New Roman', serif; font-size:14px; letter-spacing:0.3em; color:${BRAND.brass}; text-transform:uppercase; margin-bottom:8px; }
  h1 { font-family: Georgia, 'Times New Roman', serif; font-weight:400; font-size:28px; line-height:1.15; margin:0 0 18px; color:${BRAND.espresso}; }
  p { font-size:15px; line-height:1.6; color:${BRAND.inkSoft}; margin:0 0 14px; }
  .cta { display:inline-block; background:${BRAND.espresso}; color:#fff !important; padding:14px 28px; text-decoration:none; font-size:13px; letter-spacing:0.18em; text-transform:uppercase; margin:18px 0 6px; }
  .footer { text-align:center; font-size:12px; color:${BRAND.inkSoft}; margin-top:24px; line-height:1.6; }
  .footer a { color:${BRAND.brass}; }
</style>
</head>
<body>
<span style="display:none;font-size:1px;color:#fff;max-height:0;max-width:0;opacity:0;overflow:hidden">${escapeHtml(preheader || "")}</span>
<div class="wrap">
  <div class="card">
    <div class="brand">Stately Shades</div>
    <h1>${title}</h1>
    ${body}
    ${ctaUrl ? `<p style="text-align:center;margin-top:24px"><a class="cta" href="${ctaUrl}">${escapeHtml(ctaLabel || "Open")}</a></p>` : ""}
  </div>
  <div class="footer">
    ${footer || `Stately Shades · Gallatin, Tennessee<br/><a href="tel:+16292988241">629-298-8241</a> · <a href="mailto:hello@statelyshades.com">hello@statelyshades.com</a>`}
  </div>
</div>
</body>
</html>`;
}

export function escapeHtml(s) {
  if (s == null) return "";
  return String(s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}
