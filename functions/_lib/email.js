// Resend wrapper + branded HTML email templates.
//
// Env vars (Cloudflare Pages secrets):
//   RESEND_API_KEY        — re_xxxxxxxx
//   RESEND_FROM           — fallback to "Stately Shades <onboarding@resend.dev>"
//                           Once statelyshades.com is verified on Resend, set
//                           this to "Stately Shades <hello@statelyshades.com>"
//                           and customer-facing mail flips to the branded
//                           domain with zero code change.
//   RESEND_DEFAULT_REPLY  — defaults to "hello@statelyshades.com" so replies
//                           come back to the real mailbox even when sending
//                           from the resend.dev sandbox sender.
//
// History: we used Purelymail until their public /api/v0/sendMail endpoint
// went 404 in May 2026. Resend gives a clean REST API + Cloudflare-friendly
// deliverability and is free up to 3k/mo.

const RESEND_ENDPOINT = "https://api.resend.com/emails";
const DEFAULT_FROM = "Stately Shades <onboarding@resend.dev>";
const DEFAULT_REPLY = "hello@statelyshades.com";

// Best-effort mail send. Callers `await sendEmail(...)` but we never throw —
// every code path here resolves so a downstream API never crashes because the
// mail provider is unreachable or rejecting. The return shape is informational
// only: { skipped, status, json, error } — most callers ignore it.
export async function sendEmail(env, { to, subject, html, text, replyTo, attachments }) {
  if (!env.RESEND_API_KEY) {
    console.warn("[email] RESEND_API_KEY missing — skipping send");
    return { skipped: true, reason: "no_api_key" };
  }
  const from = env.RESEND_FROM || DEFAULT_FROM;
  const body = {
    from,
    to: Array.isArray(to) ? to : [to],
    subject,
    html: html || undefined,
    text: text || (html ? stripHtml(html) : undefined),
    reply_to: replyTo || env.RESEND_DEFAULT_REPLY || DEFAULT_REPLY,
  };
  // Resend supports attachments as { filename, content (base64) }
  if (attachments && attachments.length) body.attachments = attachments;

  try {
    const res = await fetch(RESEND_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${env.RESEND_API_KEY}`,
      },
      body: JSON.stringify(body),
    });
    const raw = await res.text().catch(() => "");
    let json;
    try { json = JSON.parse(raw); } catch { json = { raw: raw.slice(0, 200) }; }
    if (!res.ok) {
      console.error("[email] Resend send failed:", res.status, raw.slice(0, 200));
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
