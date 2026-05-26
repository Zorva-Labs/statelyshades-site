// ============================================================
// Stately Shades CRM — Tave-style app shell
// Loads on every /crm/ page. Renders the top nav, mounts the
// dashboard/section content, handles auth, global search, etc.
// ============================================================

const NAV = [
  { href: "/crm/",            label: "Dashboard", match: ["/crm/", "/crm/index.html"], icon: iconDash() },
  { href: "/crm/pipeline.html", label: "Pipeline", icon: iconKanban() },
  { href: "/crm/leads.html",  label: "Leads", icon: iconLead() },
  { href: "/crm/contacts.html", label: "Contacts", icon: iconUsers() },
  { href: "/crm/projects.html", label: "Jobs", icon: iconBriefcase() },
  { href: "/crm/calendar.html", label: "Calendar", icon: iconCal() },
  { href: "/crm/estimates.html", label: "Estimates", icon: iconDoc() },
  { href: "/crm/proposals.html", label: "Proposals", icon: iconDoc() },
  { href: "/crm/contracts.html", label: "Contracts", icon: iconDoc() },
  { href: "/crm/products.html", label: "Products", icon: iconBox() },
  { href: "/crm/templates.html", label: "Templates", icon: iconMail() },
  { href: "/crm/activity.html", label: "Activity", icon: iconActivity() },
];

// Sidebar groups — all links visible (we have room in the vertical rail)
const NAV_GROUPS = [
  { label: null, items: ["/crm/", "/crm/pipeline.html"] },
  { label: "People", items: ["/crm/leads.html", "/crm/contacts.html", "/crm/projects.html"] },
  { label: "Sales", items: ["/crm/estimates.html", "/crm/proposals.html", "/crm/contracts.html"] },
  { label: "Operations", items: ["/crm/calendar.html", "/crm/availability.html"] },
  { label: "Setup", items: ["/crm/products.html", "/crm/templates.html", "/crm/activity.html"] },
];

const QUICK_ADD = [
  { label: "New job", href: "/crm/contacts.html?action=new-job", kbd: "J", icon: iconBriefcase() },
  { label: "New contact", href: "/crm/contacts.html?action=new", kbd: "C", icon: iconUsers() },
  { label: "Book appointment", href: "/crm/calendar.html?action=new", kbd: "A", icon: iconCal() },
  { label: "New estimate", href: "/crm/projects.html?action=new-estimate", kbd: "E", icon: iconDoc() },
  { label: "New proposal", href: "/crm/projects.html?action=new-proposal", kbd: "P", icon: iconDoc() },
  { label: "New contract", href: "/crm/projects.html?action=new-contract", kbd: "K", icon: iconDoc() },
];

// ============================================================
// Auth + fetch
// ============================================================
async function fetchJSON(url, opts = {}) {
  const res = await fetch(url, {
    credentials: "same-origin",
    ...opts,
    headers: { "Content-Type": "application/json", Accept: "application/json", ...(opts.headers || {}) },
  });
  if (res.status === 401) {
    if (!location.pathname.endsWith("/login.html")) {
      location.href = "/crm/login.html?next=" + encodeURIComponent(location.pathname + location.search);
    }
    throw new Error("Unauthorized");
  }
  const body = (res.headers.get("content-type") || "").includes("json") ? await res.json() : await res.text();
  if (!res.ok) throw new Error((body && body.error) || "HTTP " + res.status);
  return body;
}

// ============================================================
// Mount: builds top nav + page shell, returns the user
// ============================================================
async function mount({ title = "", subtitle = "", actions = "", wide = false } = {}) {
  const me = await fetchJSON("/api/auth/me").catch(() => null);
  if (!me) return null;
  document.title = `${title} · Stately Shades CRM`;
  const path = location.pathname;
  const navByHref = Object.fromEntries(NAV.map((n) => [n.href, n]));
  const groupHtml = NAV_GROUPS.map((g) => `
    ${g.label ? `<div class="tnav__section-label">${esc(g.label)}</div>` : ""}
    ${g.items.map((href) => navByHref[href] ? navLink(navByHref[href], path) : "").join("")}
  `).join("");

  document.body.innerHTML = `
    <nav class="tnav">
      <a href="/crm/" class="tnav__brand">
        <span class="tnav__brand-mono">S</span>
        <span>Stately</span>
      </a>
      <div class="tnav__search">
        ${iconSearch()}
        <input type="search" id="g-search" placeholder="Search…" autocomplete="off" />
        <span class="tnav__search-kbd">⌘K</span>
        <div class="tnav__results" id="g-results"></div>
      </div>
      <div class="tnav__links">${groupHtml}</div>
      <div class="tnav__spacer"></div>
      <div class="tnav__quickadd">
        <button class="tnav__quickadd-btn" id="quickadd-btn" aria-label="Quick add" title="New (N)">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
        </button>
        <div class="tnav__quickadd-menu" id="quickadd-menu">
          ${QUICK_ADD.map((q) => `<a class="tnav__quickadd-item" href="${q.href}">${q.icon}<span>${esc(q.label)}</span><span class="kbd">${q.kbd}</span></a>`).join("")}
        </div>
      </div>
      <div class="tnav__user">
        <button class="tnav__user-btn" id="user-btn" data-init="${esc(initials(me.user.email))}" aria-label="User menu" title="${esc(me.user.email)}">
          <span>${esc(me.user.display_name || me.user.email.split("@")[0])}</span>
        </button>
        <div class="tnav__user-menu" id="user-menu">
          <div class="tnav__user-info">
            <strong>${esc(me.user.display_name || me.user.email)}</strong>
            <span>${esc(me.user.email)}</span>
          </div>
          <button onclick="SSCrm.logout()">Sign out</button>
        </div>
      </div>
    </nav>
    <main class="app ${wide ? "app--wide" : ""}">
      <header class="page-head">
        <div>
          <h1 id="page-title">${title}</h1>
          ${subtitle ? `<div class="sub">${subtitle}</div>` : ""}
        </div>
        <div class="actions">${actions}</div>
      </header>
      <div id="page"></div>
    </main>
  `;
  wireNav();
  return me.user;
}

function navLink(n, currentPath) {
  const matches = n.match ? n.match.includes(currentPath) : currentPath === n.href || currentPath.startsWith(n.href.replace(".html", ""));
  return `<a class="tnav__link ${matches ? "is-active" : ""}" href="${n.href}">${n.icon}<span>${esc(n.label)}</span></a>`;
}

function moreMenu(path) {
  const extras = NAV.filter((n) => !PRIMARY_NAV.includes(n.href));
  if (!extras.length) return "";
  const anyActive = extras.some((n) => path === n.href);
  return `
    <div style="position:relative" class="js-more">
      <button class="tnav__link" style="background:transparent;border:0;cursor:pointer;${anyActive ? "color:var(--accent-ink);background:var(--accent-soft);" : ""}" onclick="this.nextElementSibling.classList.toggle('is-open');event.stopPropagation()">
        More
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
      </button>
      <div class="tnav__quickadd-menu" style="left:0;right:auto">
        ${extras.map((n) => `<a class="tnav__quickadd-item" href="${n.href}">${n.icon}<span>${esc(n.label)}</span></a>`).join("")}
      </div>
    </div>
  `;
}

function wireNav() {
  // Quick-add toggle
  const qBtn = document.getElementById("quickadd-btn");
  const qMenu = document.getElementById("quickadd-menu");
  qBtn?.addEventListener("click", (e) => { e.stopPropagation(); qMenu.classList.toggle("is-open"); });

  // User menu toggle
  const uBtn = document.getElementById("user-btn");
  const uMenu = document.getElementById("user-menu");
  uBtn?.addEventListener("click", (e) => { e.stopPropagation(); uMenu.classList.toggle("is-open"); });

  // Close any open dropdown on outside click
  document.addEventListener("click", () => {
    qMenu?.classList.remove("is-open");
    uMenu?.classList.remove("is-open");
    document.querySelectorAll(".js-more .tnav__quickadd-menu").forEach((m) => m.classList.remove("is-open"));
    document.getElementById("g-results")?.classList.remove("is-open");
  });

  // Global search
  const search = document.getElementById("g-search");
  const results = document.getElementById("g-results");
  let debTimer;
  search?.addEventListener("input", () => {
    clearTimeout(debTimer);
    debTimer = setTimeout(async () => {
      const q = search.value.trim();
      if (q.length < 2) { results.classList.remove("is-open"); return; }
      try {
        const { results: data } = await fetchJSON("/api/search?q=" + encodeURIComponent(q));
        renderSearchResults(data);
      } catch (e) { /* swallow */ }
    }, 200);
  });
  search?.addEventListener("focus", () => { if (search.value.trim().length >= 2) results.classList.add("is-open"); });

  // ⌘K / Ctrl+K to focus search
  document.addEventListener("keydown", (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === "k") {
      e.preventDefault();
      search?.focus();
      search?.select();
    }
    // Escape closes menus
    if (e.key === "Escape") {
      qMenu?.classList.remove("is-open");
      uMenu?.classList.remove("is-open");
      results?.classList.remove("is-open");
    }
  });
}

function renderSearchResults(data) {
  const results = document.getElementById("g-results");
  if (!results) return;
  const groups = [];
  if (data.contacts?.length) groups.push({ label: "Contacts", items: data.contacts.map((c) => ({ url: "/crm/contact.html?id=" + c.id, label: c.name, meta: c.email })) });
  if (data.projects?.length) groups.push({ label: "Jobs", items: data.projects.map((p) => ({ url: "/crm/project.html?id=" + p.id, label: p.name, meta: p.contact_name })) });
  if (data.estimates?.length) groups.push({ label: "Estimates", items: data.estimates.map((e) => ({ url: "/crm/estimate.html?id=" + e.id, label: e.number, meta: e.contact_name })) });
  if (data.proposals?.length) groups.push({ label: "Proposals", items: data.proposals.map((p) => ({ url: "/crm/proposal.html?id=" + p.id, label: p.number, meta: p.contact_name })) });
  if (data.contracts?.length) groups.push({ label: "Contracts", items: data.contracts.map((c) => ({ url: "/crm/contract.html?id=" + c.id, label: c.number, meta: c.contact_name })) });
  if (data.leads?.length) groups.push({ label: "Leads", items: data.leads.map((l) => ({ url: "/crm/lead.html?id=" + l.id, label: l.name, meta: l.email })) });

  if (!groups.length) {
    results.innerHTML = `<div class="tnav__results-empty">No results</div>`;
  } else {
    results.innerHTML = groups.map((g) => `
      <div class="tnav__results-group">
        <span class="tnav__results-label">${esc(g.label)}</span>
        ${g.items.map((i) => `<a class="tnav__results-item" href="${i.url}">${esc(i.label)}<span class="meta">· ${esc(i.meta || "")}</span></a>`).join("")}
      </div>
    `).join("");
  }
  results.classList.add("is-open");
}

// ============================================================
// Utilities
// ============================================================
function fmtMoney(cents) { if (cents == null) return "—"; return "$" + (cents / 100).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }); }
function parseMoney(s) { const n = Number(String(s || "").replace(/[^0-9.\-]/g, "")); return Math.round((isNaN(n) ? 0 : n) * 100); }
function fmtMoneyShort(cents) { if (cents == null) return "—"; const v = cents / 100; if (Math.abs(v) >= 10000) return "$" + Math.round(v / 1000) + "k"; return "$" + v.toLocaleString("en-US", { minimumFractionDigits: 0, maximumFractionDigits: 0 }); }
function fmtDate(iso) {
  if (!iso) return "";
  const d = new Date((iso + "").replace(" ", "T") + (iso.includes("T") || iso.includes("Z") ? "" : "Z"));
  const now = new Date();
  const diff = (now - d) / 1000;
  if (diff < 60) return "just now";
  if (diff < 3600) return Math.floor(diff / 60) + "m ago";
  if (diff < 86400) return Math.floor(diff / 3600) + "h ago";
  if (diff < 86400 * 7) return Math.floor(diff / 86400) + "d ago";
  return d.toLocaleDateString(undefined, { month: "short", day: "numeric", year: d.getFullYear() === now.getFullYear() ? undefined : "numeric" });
}
function fmtDateTime(iso) { if (!iso) return ""; const d = new Date((iso + "").replace(" ", "T")); return d.toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" }); }
function fmtTime(iso) { if (!iso) return ""; const [, t] = iso.split("T"); const [h, m] = (t || "00:00").split(":").map((n) => parseInt(n, 10)); const ap = h < 12 ? "am" : "pm"; return `${((h + 11) % 12) + 1}:${String(m).padStart(2, "0")} ${ap}`; }
function esc(s) {
  if (s == null) return "";
  return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;").replace(/'/g, "&#39;");
}
function pill(s) { return `<span class="pill" data-s="${esc(s)}">${esc((s || "").replace(/_/g, " "))}</span>`; }
function initials(email) { return (email || "?").slice(0, 1).toUpperCase(); }
async function logout() {
  try { await fetch("/api/auth/logout", { method: "POST", credentials: "same-origin" }); } catch (_) {}
  location.href = "/crm/login.html";
}

// Toast
function toast(msg, kind = "info") {
  let host = document.querySelector(".toast-host");
  if (!host) { host = document.createElement("div"); host.className = "toast-host"; document.body.appendChild(host); }
  const t = document.createElement("div"); t.className = `toast toast--${kind}`; t.textContent = msg;
  host.appendChild(t);
  setTimeout(() => { t.classList.add("toast--out"); setTimeout(() => t.remove(), 320); }, 2800);
}

function confirmDialog(msg) {
  return new Promise((resolve) => {
    const bg = document.createElement("div");
    bg.className = "modal-bg";
    bg.innerHTML = `<div class="modal"><div class="modal-body"><p style="margin:0">${esc(msg)}</p></div><div class="modal-foot"><button class="btn ghost" data-no>Cancel</button><button class="btn danger" data-yes>Confirm</button></div></div>`;
    document.body.appendChild(bg);
    bg.querySelector("[data-no]").onclick = () => { bg.remove(); resolve(false); };
    bg.querySelector("[data-yes]").onclick = () => { bg.remove(); resolve(true); };
    bg.addEventListener("click", (e) => { if (e.target === bg) { bg.remove(); resolve(false); } });
  });
}

// ============================================================
// Status taxonomies
// ============================================================
const PROJECT_STATUSES = [
  { key: "new",            label: "New" },
  { key: "scheduled",      label: "Consult Booked" },
  { key: "measured",       label: "Measured" },
  { key: "quoted",         label: "Quoted" },
  { key: "proposed",       label: "Proposed" },
  { key: "contracted",     label: "Booked" },          // contracted = job is booked
  { key: "installing",     label: "Installing" },
  { key: "completed",      label: "Completed" },
  { key: "lost",           label: "Lost" },
];

// ============================================================
// Icons (inline SVG)
// ============================================================
function iconDash() { return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>`; }
function iconKanban() { return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="3" x2="3" y2="21"/><line x1="9" y1="3" x2="9" y2="15"/><line x1="15" y1="3" x2="15" y2="18"/><line x1="21" y1="3" x2="21" y2="13"/></svg>`; }
function iconLead() { return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>`; }
function iconUsers() { return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>`; }
function iconBriefcase() { return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>`; }
function iconCal() { return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>`; }
function iconDoc() { return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>`; }
function iconBox() { return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/></svg>`; }
function iconMail() { return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22 6 12 13 2 6"/></svg>`; }
function iconActivity() { return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>`; }
function iconSearch() { return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>`; }

// Export
window.SSCrm = {
  fetchJSON, mount, fmtMoney, fmtMoneyShort, parseMoney, fmtDate, fmtDateTime, fmtTime, esc, pill, logout, toast, confirmDialog,
  PROJECT_STATUSES,
};
