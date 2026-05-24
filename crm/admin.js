// Shared admin JS — auth check, fetch helpers, formatting
const STATUS_LABELS = {
  new: "New",
  contacted: "Contacted",
  quoted: "Quoted",
  scheduled: "Scheduled",
  installed: "Installed",
  won: "Won",
  lost: "Lost",
  spam: "Spam",
};
const STATUS_ORDER = ["new", "contacted", "quoted", "scheduled", "installed", "won", "lost", "spam"];

async function fetchJSON(url, opts = {}) {
  const res = await fetch(url, {
    credentials: "same-origin",
    ...opts,
    headers: { "Content-Type": "application/json", "Accept": "application/json", ...(opts.headers || {}) },
  });
  if (res.status === 401) {
    if (!location.pathname.endsWith("/login.html")) {
      location.href = "/crm/login.html?next=" + encodeURIComponent(location.pathname + location.search);
    }
    throw new Error("Unauthorized");
  }
  const ct = res.headers.get("content-type") || "";
  const body = ct.includes("json") ? await res.json() : await res.text();
  if (!res.ok) throw new Error((body && body.error) || ("HTTP " + res.status));
  return body;
}

function fmtDate(iso) {
  if (!iso) return "";
  const d = new Date(iso.replace(" ", "T") + "Z");
  const now = new Date();
  const diff = (now - d) / 1000;
  if (diff < 60) return "just now";
  if (diff < 3600) return Math.floor(diff / 60) + "m ago";
  if (diff < 86400) return Math.floor(diff / 3600) + "h ago";
  if (diff < 86400 * 7) return Math.floor(diff / 86400) + "d ago";
  return d.toLocaleDateString(undefined, { month: "short", day: "numeric", year: d.getFullYear() === now.getFullYear() ? undefined : "numeric" });
}

function fmtDateTime(iso) {
  if (!iso) return "";
  const d = new Date(iso.replace(" ", "T") + "Z");
  return d.toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" });
}

function esc(s) {
  return String(s == null ? "" : s)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function pill(status) {
  return `<span class="pill" data-status="${esc(status)}">${esc(STATUS_LABELS[status] || status)}</span>`;
}

async function logout() {
  try { await fetch("/api/auth/logout", { method: "POST", credentials: "same-origin" }); } catch (_) {}
  location.href = "/crm/login.html";
}

// Render the shared sidebar nav and load user + status counts
async function renderSidebar({ activeStatus = null } = {}) {
  const me = await fetchJSON("/api/auth/me");
  document.querySelectorAll("[data-user-email]").forEach((el) => { el.textContent = me.user.email; });

  // Use the leads endpoint to grab counts; cheap query
  let counts = {};
  try {
    const { counts: c } = await fetchJSON("/api/leads?limit=1");
    counts = c || {};
  } catch (_) {}

  const section = document.querySelector(".js-status-nav");
  if (section) {
    const total = Object.values(counts).reduce((a, b) => a + b, 0);
    const allActive = activeStatus === null ? " is-active" : "";
    let html = `<a class="admin__nav-link${allActive}" href="/crm/">All <span class="admin__nav-count">${total}</span></a>`;
    for (const s of STATUS_ORDER) {
      const n = counts[s] || 0;
      const isActive = activeStatus === s ? " is-active" : "";
      html += `<a class="admin__nav-link${isActive}" href="/crm/?status=${s}">${STATUS_LABELS[s]} <span class="admin__nav-count">${n}</span></a>`;
    }
    section.innerHTML = html;
  }
}

window.SSAdmin = { fetchJSON, fmtDate, fmtDateTime, esc, pill, logout, renderSidebar, STATUS_LABELS, STATUS_ORDER };
