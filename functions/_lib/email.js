// Purelymail SMTP transport for Cloudflare Pages Functions.
//
// We can't call Purelymail's REST API anymore (their public /api/v0/sendMail
// endpoint went 404 in May 2026), but their SMTP server still works. We use
// Cloudflare's outbound TCP socket API (`cloudflare:sockets`) to speak
// SMTP-AUTH-LOGIN with STARTTLS on port 587.
//
// Env vars (Cloudflare Pages secrets — set via `wrangler pages secret put`):
//   PURELYMAIL_USER     — full mailbox address, e.g. "hello@statelyshades.com"
//   PURELYMAIL_PASSWORD — mailbox password (same as webmail login)
//   MAIL_FROM           — optional; defaults to "Stately Shades <hello@statelyshades.com>"
//   MAIL_DEFAULT_REPLY  — optional; defaults to PURELYMAIL_USER
//
// History:
//   - Originally used Purelymail REST API (now dead).
//   - Briefly tried Resend sandbox sender (works but costs $$ at scale).
//   - Now SMTP direct to Purelymail (free, uses existing mailbox).

import { connect } from "cloudflare:sockets";

const SMTP_HOST = "smtp.purelymail.com";
const SMTP_PORT = 587;
const DEFAULT_FROM = "Stately Shades <hello@statelyshades.com>";
const CRLF = "\r\n";

// Best-effort mail send. Never throws. Returns { status, json, messageId } on
// success or { skipped, error } on failure. messageId is the RFC 5322 header
// value we generated for this send — callers use it for threading.
//
// Options:
//   to, cc, bcc       — string or array of recipients (each may be "Name <a@x>")
//   subject, html, text
//   replyTo           — defaults to env.MAIL_DEFAULT_REPLY → PURELYMAIL_USER
//   messageId         — pass a pre-generated <id@host> to override (else random)
//   inReplyTo         — parent Message-ID, sets In-Reply-To + References headers
//   references        — full References chain (whitespace separated)
//   from              — full From header (defaults to MAIL_FROM env)
//   attachments       — [{ filename, content (b64), content_type }]
export async function sendEmail(env, {
  to, cc, bcc, subject, html, text, replyTo, attachments,
  messageId, inReplyTo, references, from,
}) {
  if (!env.PURELYMAIL_USER || !env.PURELYMAIL_PASSWORD) {
    console.warn("[email] PURELYMAIL_USER/PASSWORD missing — skipping send");
    return { skipped: true, reason: "no_creds" };
  }
  const fromHeader = from || env.MAIL_FROM || DEFAULT_FROM;
  const toList  = Array.isArray(to)  ? to  : (to ? [to] : []);
  const ccList  = Array.isArray(cc)  ? cc  : (cc ? [cc] : []);
  const bccList = Array.isArray(bcc) ? bcc : (bcc ? [bcc] : []);
  const reply = replyTo || env.MAIL_DEFAULT_REPLY || env.PURELYMAIL_USER;
  // SMTP envelope MAIL FROM uses the auth'd mailbox so Purelymail never rejects
  // the submission ("550 sender not allowed"). The visible From: header can be
  // anything on the same domain (e.g. crm@statelyshades.com) — this is how we
  // break the self-loop when From and To would otherwise both be hello@.
  const envelopeFromAddr = env.PURELYMAIL_USER;
  const mid = messageId || makeMessageId();

  // RCPT TO list includes To + Cc + Bcc (envelope, not headers — Bcc never in headers)
  const envelopeRecipients = [...toList, ...ccList, ...bccList].map(extractAddr);
  if (envelopeRecipients.length === 0) {
    return { skipped: true, error: "no_recipients" };
  }

  const message = buildMimeMessage({
    from: fromHeader, to: toList, cc: ccList,
    replyTo: reply, subject, html, text, attachments,
    messageId: mid, inReplyTo, references,
  });

  try {
    const result = await smtpSend({
      host: SMTP_HOST,
      port: SMTP_PORT,
      user: env.PURELYMAIL_USER,
      password: env.PURELYMAIL_PASSWORD,
      fromAddr: envelopeFromAddr,                  // envelope MAIL FROM (auth user)
      recipients: envelopeRecipients,
      message,                                      // body contains the visible From: header
    });
    return { status: 250, json: result, messageId: mid };
  } catch (e) {
    console.error("[email] SMTP send failed:", e?.message || e);
    return { skipped: true, error: e?.message || "smtp_failed", messageId: mid };
  }
}

// Generate an RFC 5322 Message-ID — exported so callers can pre-generate one
// when they want to insert into D1 with the same ID before/while sending.
export function makeMessageId(domain = "statelyshades.com") {
  return `<${Math.random().toString(36).slice(2, 14)}.${Date.now().toString(36)}@${domain}>`;
}

// ────────────────────────────────────────────────────────────────────
// SMTP client — minimal AUTH LOGIN + STARTTLS conversation
// ────────────────────────────────────────────────────────────────────

async function smtpSend({ host, port, user, password, fromAddr, recipients, message }) {
  // Open as plaintext first; STARTTLS upgrades the connection mid-session.
  const socket = connect(`${host}:${port}`, { secureTransport: "starttls", allowHalfOpen: false });

  const writer = socket.writable.getWriter();
  const reader = socket.readable.getReader();
  const encoder = new TextEncoder();
  const decoder = new TextDecoder();

  // Buffer for inbound bytes — SMTP responses can span multiple chunks
  let inbuf = "";
  async function readLine() {
    while (true) {
      const idx = inbuf.indexOf(CRLF);
      if (idx !== -1) {
        const line = inbuf.slice(0, idx);
        inbuf = inbuf.slice(idx + 2);
        return line;
      }
      const { value, done } = await reader.read();
      if (done) throw new Error("SMTP socket closed unexpectedly");
      inbuf += decoder.decode(value, { stream: true });
    }
  }
  // Read a full SMTP reply (handles multi-line "250-ENHANCEDSTATUS / 250 OK")
  async function readReply() {
    const lines = [];
    while (true) {
      const line = await readLine();
      lines.push(line);
      // Continuation lines have a hyphen after the 3-digit code; the final
      // line in a multi-line reply has a space.
      if (line.length < 4 || line[3] === " ") break;
    }
    const code = parseInt(lines[lines.length - 1].slice(0, 3), 10);
    return { code, lines, raw: lines.join("\n") };
  }
  async function send(cmd) { await writer.write(encoder.encode(cmd + CRLF)); }
  function assertOk(reply, expectCode, step) {
    if (reply.code !== expectCode) {
      throw new Error(`SMTP ${step}: expected ${expectCode}, got ${reply.code}: ${reply.raw.slice(0, 200)}`);
    }
  }

  try {
    // 1) Greeting
    assertOk(await readReply(), 220, "greeting");

    // 2) EHLO (plaintext)
    await send(`EHLO statelyshades.com`);
    assertOk(await readReply(), 250, "EHLO-plain");

    // 3) STARTTLS — server replies 220, then we upgrade the socket
    await send("STARTTLS");
    assertOk(await readReply(), 220, "STARTTLS");
    writer.releaseLock();
    reader.releaseLock();
    const tlsSocket = socket.startTls();
    return await smtpAuthAndSend({ socket: tlsSocket, user, password, fromAddr, recipients, message });
  } catch (e) {
    try { writer.releaseLock(); } catch (_) {}
    try { reader.releaseLock(); } catch (_) {}
    try { await socket.close(); } catch (_) {}
    throw e;
  }
}

// Post-STARTTLS leg: EHLO again, AUTH LOGIN, MAIL FROM, RCPT TO, DATA, QUIT
async function smtpAuthAndSend({ socket, user, password, fromAddr, recipients, message }) {
  const writer = socket.writable.getWriter();
  const reader = socket.readable.getReader();
  const encoder = new TextEncoder();
  const decoder = new TextDecoder();
  let inbuf = "";
  async function readLine() {
    while (true) {
      const idx = inbuf.indexOf(CRLF);
      if (idx !== -1) {
        const line = inbuf.slice(0, idx);
        inbuf = inbuf.slice(idx + 2);
        return line;
      }
      const { value, done } = await reader.read();
      if (done) throw new Error("SMTP TLS socket closed unexpectedly");
      inbuf += decoder.decode(value, { stream: true });
    }
  }
  async function readReply() {
    const lines = [];
    while (true) {
      const line = await readLine();
      lines.push(line);
      if (line.length < 4 || line[3] === " ") break;
    }
    const code = parseInt(lines[lines.length - 1].slice(0, 3), 10);
    return { code, lines, raw: lines.join("\n") };
  }
  async function send(cmd) { await writer.write(encoder.encode(cmd + CRLF)); }
  function assertOk(reply, expectCode, step) {
    if (reply.code !== expectCode) {
      throw new Error(`SMTP ${step}: expected ${expectCode}, got ${reply.code}: ${reply.raw.slice(0, 200)}`);
    }
  }

  try {
    // EHLO over TLS so the server advertises AUTH LOGIN
    await send(`EHLO statelyshades.com`);
    assertOk(await readReply(), 250, "EHLO-tls");

    // AUTH LOGIN — server asks for username (base64), then password (base64)
    await send("AUTH LOGIN");
    assertOk(await readReply(), 334, "AUTH-LOGIN-init");
    await send(btoa(user));
    assertOk(await readReply(), 334, "AUTH-LOGIN-user");
    await send(btoa(password));
    assertOk(await readReply(), 235, "AUTH-LOGIN-pass");

    // MAIL FROM
    await send(`MAIL FROM:<${fromAddr}>`);
    assertOk(await readReply(), 250, "MAIL-FROM");

    // RCPT TO (one per recipient)
    for (const rcpt of recipients) {
      await send(`RCPT TO:<${extractAddr(rcpt)}>`);
      assertOk(await readReply(), 250, "RCPT-TO");
    }

    // DATA → 354 → message body → "."
    await send("DATA");
    assertOk(await readReply(), 354, "DATA-init");
    // Dot-stuff: lines beginning with "." get prefixed with another "." per RFC 5321
    const dotStuffed = message.replace(/\r\n\./g, "\r\n..");
    await writer.write(encoder.encode(dotStuffed + CRLF + "." + CRLF));
    assertOk(await readReply(), 250, "DATA-end");

    // QUIT
    await send("QUIT");
    // 221 expected but some servers close before responding; ignore failures
    try { await readReply(); } catch (_) {}

    writer.releaseLock();
    reader.releaseLock();
    try { await socket.close(); } catch (_) {}
    return { ok: true };
  } catch (e) {
    try { writer.releaseLock(); } catch (_) {}
    try { reader.releaseLock(); } catch (_) {}
    try { await socket.close(); } catch (_) {}
    throw e;
  }
}

// ────────────────────────────────────────────────────────────────────
// MIME message builder
// ────────────────────────────────────────────────────────────────────

function buildMimeMessage({ from, to, cc, replyTo, subject, html, text, attachments, messageId, inReplyTo, references }) {
  const boundary = "ssbnd_" + Math.random().toString(36).slice(2, 10) + Date.now().toString(36);
  const date = new Date().toUTCString();
  const mid = messageId || makeMessageId();
  const toLine  = (Array.isArray(to) ? to : [to]).join(", ");
  const ccLine  = cc && cc.length ? (Array.isArray(cc) ? cc : [cc]).join(", ") : "";

  const hasHtml = !!html;
  const hasText = !!(text || hasHtml);

  const headers = [
    `From: ${from}`,
    `To: ${toLine}`,
    ccLine ? `Cc: ${ccLine}` : "",
    replyTo ? `Reply-To: ${replyTo}` : "",
    `Subject: ${encodeMimeHeader(subject || "(no subject)")}`,
    `Date: ${date}`,
    `Message-ID: ${mid}`,
    inReplyTo ? `In-Reply-To: ${inReplyTo}` : "",
    references ? `References: ${references}` : (inReplyTo ? `References: ${inReplyTo}` : ""),
    `MIME-Version: 1.0`,
  ].filter(Boolean);

  // Single-part (text-only or html-only) — keep the envelope simple
  if (hasText && !hasHtml) {
    headers.push(`Content-Type: text/plain; charset="utf-8"`);
    headers.push(`Content-Transfer-Encoding: quoted-printable`);
    return headers.join(CRLF) + CRLF + CRLF + qpEncode(text);
  }
  if (hasHtml && !hasText) {
    headers.push(`Content-Type: text/html; charset="utf-8"`);
    headers.push(`Content-Transfer-Encoding: quoted-printable`);
    return headers.join(CRLF) + CRLF + CRLF + qpEncode(html);
  }

  // Multipart/alternative — both text + html
  headers.push(`Content-Type: multipart/alternative; boundary="${boundary}"`);
  const parts = [
    `--${boundary}`,
    `Content-Type: text/plain; charset="utf-8"`,
    `Content-Transfer-Encoding: quoted-printable`,
    ``,
    qpEncode(text || stripHtml(html)),
    ``,
    `--${boundary}`,
    `Content-Type: text/html; charset="utf-8"`,
    `Content-Transfer-Encoding: quoted-printable`,
    ``,
    qpEncode(html),
    ``,
    `--${boundary}--`,
  ];
  return headers.join(CRLF) + CRLF + CRLF + parts.join(CRLF);
}

// ────────────────────────────────────────────────────────────────────
// Helpers
// ────────────────────────────────────────────────────────────────────

// Extract the bare addr-spec from either "Name <addr@x>" or "addr@x"
function extractAddr(s) {
  const m = String(s || "").match(/<([^>]+)>/);
  return (m ? m[1] : s).trim();
}

// Quoted-printable encode for MIME body parts. RFC 2045 — only chars
// outside printable ASCII (and =) get escaped. Line length capped at 76.
function qpEncode(s) {
  if (s == null) return "";
  const str = String(s);
  const out = [];
  let lineLen = 0;
  for (let i = 0; i < str.length; i++) {
    const ch = str[i];
    const code = ch.charCodeAt(0);
    let enc;
    if (ch === "\r" || ch === "\n") {
      out.push(ch);
      lineLen = 0;
      continue;
    }
    if (code === 0x3D /* = */ || code < 32 || code > 126) {
      // Multi-byte UTF-8 → encode each byte separately
      const bytes = new TextEncoder().encode(ch);
      enc = "";
      for (const b of bytes) enc += "=" + b.toString(16).toUpperCase().padStart(2, "0");
    } else {
      enc = ch;
    }
    if (lineLen + enc.length > 75) {
      out.push("=" + CRLF); // soft line break
      lineLen = 0;
    }
    out.push(enc);
    lineLen += enc.length;
  }
  return out.join("");
}

// Encode non-ASCII subject headers as RFC 2047 encoded-word (if needed)
function encodeMimeHeader(s) {
  if (/^[\x20-\x7E]*$/.test(s)) return s; // pure ASCII — leave alone
  // base64 UTF-8 encoded-word
  const b64 = btoa(unescape(encodeURIComponent(s)));
  return `=?UTF-8?B?${b64}?=`;
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
