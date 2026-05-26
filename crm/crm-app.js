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
  // Estimates removed — workflow is now Lead → Proposal → Contract → Booked.
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

// JS actions — no nav, opens an inline modal that creates the entity and routes to its page on success
const QUICK_ADD = [
  { label: "New contact",      action: "quickAddContact",     kbd: "C", icon: iconUsers() },
  { label: "New job",          action: "quickAddJob",         kbd: "J", icon: iconBriefcase() },
  { label: "Book appointment", action: "quickAddAppointment", kbd: "A", icon: iconCal() },
  { label: "New proposal",     action: "quickAddProposal",    kbd: "P", icon: iconDoc() },
  { label: "New contract",     action: "quickAddContract",    kbd: "K", icon: iconDoc() },
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
          ${QUICK_ADD.map((q) => `<button class="tnav__quickadd-item" type="button" onclick="SSCrm.${q.action}();document.getElementById('quickadd-menu').classList.remove('is-open')">${q.icon}<span>${esc(q.label)}</span><span class="kbd">${q.kbd}</span></button>`).join("")}
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
// ============================================================
// Quick-Add modal infrastructure
// ============================================================

// Generic modal builder: title + body HTML + array of footer buttons
function openModal({ title, body, buttons = [] }) {
  return new Promise((resolve) => {
    const bg = document.createElement("div");
    bg.className = "modal-bg";
    bg.innerHTML = `
      <div class="modal" style="max-width:560px">
        <div class="modal-head">${esc(title)}</div>
        <div class="modal-body">${body}</div>
        <div class="modal-foot">${buttons.map((b, i) => `<button class="btn ${b.kind || "ghost"}" data-i="${i}">${esc(b.label)}</button>`).join("")}</div>
      </div>
    `;
    document.body.appendChild(bg);
    const close = (v) => { bg.remove(); resolve(v); };
    buttons.forEach((b, i) => bg.querySelector(`[data-i="${i}"]`).onclick = () => close(b.value !== undefined ? b.value : i));
    bg.addEventListener("click", (e) => { if (e.target === bg) close(null); });
    bg.querySelector(".modal-body input, .modal-body select, .modal-body textarea")?.focus();
  });
}

// Contact-picker modal — type-ahead, returns selected contact or null
async function pickContact({ allowNew = true } = {}) {
  return new Promise(async (resolve) => {
    const { contacts } = await fetchJSON("/api/contacts");
    const bg = document.createElement("div");
    bg.className = "modal-bg";
    bg.innerHTML = `
      <div class="modal" style="max-width:520px">
        <div class="modal-head">Pick a contact</div>
        <div class="modal-body">
          <input type="search" id="pc-q" placeholder="Search name, email…" autocomplete="off" autofocus
                 style="width:100%;padding:9px 12px;border:1px solid var(--line-strong);border-radius:var(--r-sm);font-size:13px;margin-bottom:12px"/>
          <div id="pc-list" style="max-height:340px;overflow-y:auto;border:1px solid var(--line-soft);border-radius:var(--r-sm)"></div>
        </div>
        <div class="modal-foot">
          ${allowNew ? `<button class="btn secondary" id="pc-new">+ New contact</button>` : ""}
          <button class="btn ghost" id="pc-cancel">Cancel</button>
        </div>
      </div>
    `;
    document.body.appendChild(bg);
    const list = bg.querySelector("#pc-list");
    function render(filter = "") {
      const f = filter.toLowerCase();
      const matches = contacts.filter((c) => !f || (c.name + " " + c.email + " " + (c.phone || "")).toLowerCase().includes(f)).slice(0, 50);
      if (!matches.length) { list.innerHTML = `<div style="padding:30px;text-align:center;color:var(--ink-muted);font-size:13px">No contacts match.</div>`; return; }
      list.innerHTML = matches.map((c) => `
        <button type="button" data-id="${c.id}" style="display:block;width:100%;text-align:left;padding:10px 14px;background:transparent;border:0;border-bottom:1px solid var(--line-soft);cursor:pointer;font-size:13px">
          <strong style="color:var(--ink)">${esc(c.name)}</strong>
          <div style="color:var(--ink-soft);font-size:12px">${esc(c.email)}${c.phone ? " · " + esc(c.phone) : ""}</div>
        </button>
      `).join("");
      list.querySelectorAll("[data-id]").forEach((b) => b.onclick = () => { const c = contacts.find((x) => x.id === parseInt(b.dataset.id, 10)); bg.remove(); resolve(c); });
    }
    render();
    bg.querySelector("#pc-q").oninput = (e) => render(e.target.value);
    bg.querySelector("#pc-cancel").onclick = () => { bg.remove(); resolve(null); };
    bg.addEventListener("click", (e) => { if (e.target === bg) { bg.remove(); resolve(null); } });
    if (allowNew) {
      bg.querySelector("#pc-new").onclick = async () => {
        bg.remove();
        const c = await quickAddContact({ skipNav: true });
        resolve(c);
      };
    }
  });
}

// Job/project picker — pick from a contact's jobs (creates one if none exist)
async function pickJob(contactId) {
  const { contacts: [contact], projects } = await Promise.all([
    fetchJSON(`/api/contacts?q=`).then(async () => ({ contacts: [(await fetchJSON("/api/contacts/" + contactId)).contact] })),
    fetchJSON(`/api/projects?contact_id=${contactId}`),
  ]).then(([c, p]) => ({ ...c, ...p }));

  if (!projects.length) {
    // Auto-create one
    const name = prompt(`No job yet for ${contact.name}. Name a new job (e.g. 'Whole house', 'Kitchen + Baths'):`, "Whole house");
    if (!name) return null;
    const { id } = await fetchJSON("/api/projects", { method: "POST", body: JSON.stringify({ contact_id: contactId, name }) });
    return { id, name };
  }
  if (projects.length === 1) return projects[0];

  return new Promise((resolve) => {
    const bg = document.createElement("div");
    bg.className = "modal-bg";
    bg.innerHTML = `
      <div class="modal" style="max-width:520px">
        <div class="modal-head">Pick a job for ${esc(contact.name)}</div>
        <div class="modal-body" style="display:grid;gap:6px;max-height:340px;overflow-y:auto">
          ${projects.map((p) => `<button class="btn ghost" data-pid="${p.id}" style="justify-content:space-between;padding:10px 12px;text-align:left"><strong>${esc(p.name)}</strong><span class="muted" style="font-size:12px">${esc(p.status)}</span></button>`).join("")}
          <button class="btn secondary" data-new="1" style="margin-top:8px">+ New job</button>
        </div>
        <div class="modal-foot"><button class="btn ghost" data-cancel>Cancel</button></div>
      </div>
    `;
    document.body.appendChild(bg);
    bg.querySelectorAll("[data-pid]").forEach((b) => b.onclick = () => { bg.remove(); resolve(projects.find((p) => p.id === parseInt(b.dataset.pid, 10))); });
    bg.querySelector("[data-new]").onclick = async () => {
      bg.remove();
      const name = prompt("New job name:", "");
      if (!name) return resolve(null);
      const { id } = await fetchJSON("/api/projects", { method: "POST", body: JSON.stringify({ contact_id: contactId, name }) });
      resolve({ id, name });
    };
    bg.querySelector("[data-cancel]").onclick = () => { bg.remove(); resolve(null); };
    bg.addEventListener("click", (e) => { if (e.target === bg) { bg.remove(); resolve(null); } });
  });
}

// ---- Quick-add actions ----

async function quickAddContact({ skipNav = false } = {}) {
  const bg = document.createElement("div");
  bg.className = "modal-bg";
  bg.innerHTML = `
    <div class="modal" style="max-width:480px">
      <div class="modal-head">New contact</div>
      <div class="modal-body">
        <div class="form">
          <label><span>Full name</span><input id="qc-name" autofocus required/></label>
          <label><span>Email</span><input id="qc-email" type="email" required/></label>
          <label><span>Phone (optional)</span><input id="qc-phone" type="tel"/></label>
        </div>
      </div>
      <div class="modal-foot">
        <button class="btn ghost" data-cancel>Cancel</button>
        <button class="btn primary" data-save>Create &amp; open</button>
      </div>
    </div>
  `;
  document.body.appendChild(bg);
  return new Promise((resolve) => {
    bg.querySelector("[data-cancel]").onclick = () => { bg.remove(); resolve(null); };
    bg.querySelector("[data-save]").onclick = async () => {
      const name = bg.querySelector("#qc-name").value.trim();
      const email = bg.querySelector("#qc-email").value.trim();
      const phone = bg.querySelector("#qc-phone").value.trim();
      if (!name || !email) { toast("Name + email required", "error"); return; }
      try {
        const { id } = await fetchJSON("/api/contacts", { method: "POST", body: JSON.stringify({ name, email, phone: phone || null }) });
        bg.remove();
        if (!skipNav) location.href = "/crm/contact.html?id=" + id;
        resolve({ id, name, email, phone });
      } catch (e) { toast(e.message, "error"); }
    };
    bg.addEventListener("click", (e) => { if (e.target === bg) { bg.remove(); resolve(null); } });
  });
}

async function quickAddJob() {
  const contact = await pickContact();
  if (!contact) return;
  const name = prompt(`Job name for ${contact.name}?`, "Whole house");
  if (!name) return;
  try {
    const { id } = await fetchJSON("/api/projects", { method: "POST", body: JSON.stringify({ contact_id: contact.id, name }) });
    location.href = "/crm/project.html?id=" + id;
  } catch (e) { toast(e.message, "error"); }
}

async function quickAddAppointment() {
  const bg = document.createElement("div");
  bg.className = "modal-bg";
  // Pre-fill with tomorrow 10:00 Central
  const tomorrow = new Date(Date.now() + 86400000);
  const defaultDate = tomorrow.toISOString().slice(0, 10);
  bg.innerHTML = `
    <div class="modal" style="max-width:520px">
      <div class="modal-head">Book appointment</div>
      <div class="modal-body">
        <div class="form">
          <label><span>Customer name</span><input id="qa-name" autofocus required/></label>
          <div class="row">
            <label><span>Email</span><input id="qa-email" type="email" required/></label>
            <label><span>Phone</span><input id="qa-phone" type="tel"/></label>
          </div>
          <div class="row">
            <label><span>Date</span><input id="qa-date" type="date" value="${defaultDate}" required/></label>
            <label><span>Start time</span><input id="qa-time" type="time" value="10:00" required/></label>
          </div>
          <div class="row">
            <label><span>Duration (min)</span><input id="qa-dur" type="number" value="60" min="15" step="15"/></label>
            <label><span>Type</span>
              <select id="qa-type"><option value="consultation">Consultation</option><option value="measure">Measure</option><option value="install">Install</option><option value="service">Service</option></select>
            </label>
          </div>
          <label><span>Site address (optional)</span><input id="qa-addr"/></label>
          <label><span>Rooms (optional)</span><input id="qa-rooms" placeholder="Living, primary BR, 2 baths"/></label>
        </div>
      </div>
      <div class="modal-foot">
        <button class="btn ghost" data-cancel>Cancel</button>
        <button class="btn primary" data-save>Book it</button>
      </div>
    </div>
  `;
  document.body.appendChild(bg);
  const close = () => bg.remove();
  bg.querySelector("[data-cancel]").onclick = close;
  bg.addEventListener("click", (e) => { if (e.target === bg) close(); });
  bg.querySelector("[data-save]").onclick = async () => {
    const date = bg.querySelector("#qa-date").value;
    const time = bg.querySelector("#qa-time").value;
    const dur = parseInt(bg.querySelector("#qa-dur").value || "60", 10);
    const [h, m] = time.split(":").map((n) => parseInt(n, 10));
    const totalMin = h * 60 + m + dur;
    const endTime = `${String(Math.floor(totalMin / 60)).padStart(2, "0")}:${String(totalMin % 60).padStart(2, "0")}`;
    const body = {
      name: bg.querySelector("#qa-name").value.trim(),
      email: bg.querySelector("#qa-email").value.trim(),
      phone: bg.querySelector("#qa-phone").value.trim() || null,
      start_at: `${date}T${time}:00`,
      end_at: `${date}T${endTime}:00`,
      duration_min: dur,
      type: bg.querySelector("#qa-type").value,
      site_address: bg.querySelector("#qa-addr").value.trim() || null,
      rooms: bg.querySelector("#qa-rooms").value.trim() || null,
      status: "confirmed",
      source: "admin",
    };
    if (!body.name || !body.email) { toast("Name + email required", "error"); return; }
    try {
      await fetchJSON("/api/appointments", { method: "POST", body: JSON.stringify(body) });
      bg.remove();
      toast("Appointment booked", "success");
      if (location.pathname.includes("/calendar")) location.reload();
      else location.href = "/crm/calendar.html";
    } catch (e) { toast(e.message, "error"); }
  };
}

async function quickAddEstimate() {
  const contact = await pickContact();
  if (!contact) return;
  const job = await pickJob(contact.id);
  if (!job) return;
  try {
    const { id } = await fetchJSON("/api/estimates", { method: "POST", body: JSON.stringify({ project_id: job.id }) });
    location.href = "/crm/estimate.html?id=" + id;
  } catch (e) { toast(e.message, "error"); }
}

async function quickAddProposal() {
  const contact = await pickContact();
  if (!contact) return;
  const job = await pickJob(contact.id);
  if (!job) return;
  try {
    const { id } = await fetchJSON("/api/proposals", { method: "POST", body: JSON.stringify({ project_id: job.id }) });
    location.href = "/crm/proposal.html?id=" + id;
  } catch (e) { toast(e.message, "error"); }
}

async function quickAddContract() {
  const contact = await pickContact();
  if (!contact) return;
  const job = await pickJob(contact.id);
  if (!job) return;
  // Pick contract type
  const type = await new Promise((resolve) => {
    const bg = document.createElement("div");
    bg.className = "modal-bg";
    bg.innerHTML = `
      <div class="modal" style="max-width:520px">
        <div class="modal-head">What kind of contract?</div>
        <div class="modal-body" style="display:grid;gap:8px">
          <button class="btn secondary" data-t="custom_order" style="justify-content:flex-start;padding:12px;text-align:left;flex-direction:column;align-items:flex-start;gap:2px"><strong style="font-size:13px">Custom Order</strong><span style="font-size:12px;color:var(--ink-soft);font-weight:400">We supply &amp; install. 50% deposit.</span></button>
          <button class="btn secondary" data-t="install_only" style="justify-content:flex-start;padding:12px;text-align:left;flex-direction:column;align-items:flex-start;gap:2px"><strong style="font-size:13px">Install Only · BYO Blinds</strong><span style="font-size:12px;color:var(--ink-soft);font-weight:400">Lowes/Home Depot/Costco/Blinds.com. No deposit.</span></button>
          <button class="btn secondary" data-t="repair" style="justify-content:flex-start;padding:12px;text-align:left;flex-direction:column;align-items:flex-start;gap:2px"><strong style="font-size:13px">Repair / Service Call</strong><span style="font-size:12px;color:var(--ink-soft);font-weight:400">Service-call fee + parts.</span></button>
        </div>
        <div class="modal-foot"><button class="btn ghost" data-no>Cancel</button></div>
      </div>
    `;
    document.body.appendChild(bg);
    bg.querySelectorAll("[data-t]").forEach((b) => b.onclick = () => { bg.remove(); resolve(b.dataset.t); });
    bg.querySelector("[data-no]").onclick = () => { bg.remove(); resolve(null); };
    bg.addEventListener("click", (e) => { if (e.target === bg) { bg.remove(); resolve(null); } });
  });
  if (!type) return;
  try {
    const { id } = await fetchJSON("/api/contracts", { method: "POST", body: JSON.stringify({ project_id: job.id, contract_type: type }) });
    location.href = "/crm/contract.html?id=" + id;
  } catch (e) { toast(e.message, "error"); }
}

// ============================================================
// Product catalog picker — used by proposal / estimate / contract builders
// to pull in products, labor, and services with auto-calculated pricing
// from inch dimensions (where applicable).
// ============================================================

// Friendly category labels + display order
const CATEGORY_GROUPS = [
  { key: "plantation", label: "Plantation & Wood Shutters" },
  { key: "cellular",   label: "Cellular & Honeycomb" },
  { key: "sheer",      label: "Sheer Vanes (Silhouette/Pirouette/Luminette)" },
  { key: "woven-wood", label: "Woven Wood & Bamboo" },
  { key: "zebra",      label: "Zebra & Banded" },
  { key: "solar",      label: "Solar Shades" },
  { key: "roller",     label: "Roller Shades" },
  { key: "roman",      label: "Roman Shades" },
  { key: "real-wood",  label: "Real Wood Blinds" },
  { key: "faux-wood",  label: "Faux Wood Blinds" },
  { key: "drapery",    label: "Custom Drapery" },
  { key: "motor",      label: "Motorization & Smart Home" },
  { key: "outdoor",    label: "Outdoor Shades & Awnings" },
  { key: "install",    label: "Install Labor" },
  { key: "repair",     label: "Repair / Service Calls" },
];

// Open the picker modal and return a line-ready object, or null if cancelled
async function pickProduct() {
  const { products } = await fetchJSON("/api/products");
  return new Promise((resolve) => {
    const bg = document.createElement("div");
    bg.className = "modal-bg";
    bg.innerHTML = `
      <div class="modal" style="max-width:680px;width:100%">
        <div class="modal-head">Add from catalog</div>
        <div class="modal-body" style="padding:0">
          <div style="padding:14px 22px;border-bottom:1px solid var(--line-soft);display:flex;gap:10px;align-items:center;flex-wrap:wrap">
            <input type="search" id="pp-q" placeholder="Search by product name or SKU…" autofocus
                   style="flex:1;min-width:200px;padding:8px 12px;border:1px solid var(--line-strong);border-radius:var(--r-sm);font-size:13px"/>
            <select id="pp-cat" style="padding:8px 10px;border:1px solid var(--line-strong);border-radius:var(--r-sm);font-size:13px">
              <option value="">All categories</option>
              <optgroup label="Products">
                ${CATEGORY_GROUPS.filter((c) => !["install","repair"].includes(c.key)).map((c) => `<option value="${c.key}">${esc(c.label)}</option>`).join("")}
              </optgroup>
              <optgroup label="Labor &amp; Services">
                ${CATEGORY_GROUPS.filter((c) => ["install","repair"].includes(c.key)).map((c) => `<option value="${c.key}">${esc(c.label)}</option>`).join("")}
              </optgroup>
            </select>
          </div>
          <div id="pp-list" style="max-height:420px;overflow-y:auto"></div>
        </div>
        <div class="modal-foot">
          <button class="btn ghost" data-cancel>Cancel</button>
          <a class="btn ghost" href="/crm/products.html" target="_blank">Edit catalog →</a>
        </div>
      </div>
    `;
    document.body.appendChild(bg);
    const close = (v) => { bg.remove(); resolve(v); };
    bg.querySelector("[data-cancel]").onclick = () => close(null);
    bg.addEventListener("click", (e) => { if (e.target === bg) close(null); });
    document.addEventListener("keydown", function escClose(e) {
      if (e.key === "Escape") { close(null); document.removeEventListener("keydown", escClose); }
    });

    const list = bg.querySelector("#pp-list");
    const q = bg.querySelector("#pp-q");
    const cat = bg.querySelector("#pp-cat");

    function render() {
      const term = q.value.toLowerCase().trim();
      const catFilter = cat.value;
      const filtered = products.filter((p) => {
        if (!p.active) return false;
        if (catFilter && p.category !== catFilter) return false;
        if (!term) return true;
        return (p.name + " " + (p.sku || "") + " " + p.category).toLowerCase().includes(term);
      });
      // Group by category
      const groups = {};
      for (const p of filtered) (groups[p.category] ||= []).push(p);
      const orderedKeys = CATEGORY_GROUPS.filter((g) => groups[g.key]).map((g) => g.key);

      if (!orderedKeys.length) {
        list.innerHTML = `<p style="text-align:center;color:var(--ink-muted);padding:40px;font-size:13px">No products match. <a href="/crm/products.html" target="_blank">Add one →</a></p>`;
        return;
      }
      list.innerHTML = orderedKeys.map((k) => {
        const label = CATEGORY_GROUPS.find((g) => g.key === k)?.label || k;
        return `
          <div style="border-bottom:1px solid var(--line-soft)">
            <div style="padding:10px 22px 6px;font-family:var(--font-mono);font-size:10px;letter-spacing:0.14em;text-transform:uppercase;color:var(--ink-muted);font-weight:600">${esc(label)}</div>
            ${groups[k].map((p) => productRow(p)).join("")}
          </div>
        `;
      }).join("");
      list.querySelectorAll("[data-pp-id]").forEach((b) => b.onclick = () => pickOne(parseInt(b.dataset.ppId, 10)));
    }

    function productRow(p) {
      const priceHint = p.base_price_cents > 0 ? fmtMoney(p.base_price_cents) + " / " + (p.unit || "ea") : "—";
      return `
        <button data-pp-id="${p.id}" type="button" style="display:flex;width:100%;align-items:center;gap:12px;padding:10px 22px;background:transparent;border:0;border-bottom:1px solid var(--bg-soft);text-align:left;cursor:pointer;font-size:13px">
          <div style="flex:1;min-width:0">
            <div style="font-weight:600;color:var(--ink)">${esc(p.name)}</div>
            <div style="font-size:11px;color:var(--ink-soft);margin-top:2px">${p.sku ? esc(p.sku) + " · " : ""}${esc(p.unit || "window")}</div>
          </div>
          <div style="text-align:right;font-variant-numeric:tabular-nums;flex-shrink:0;font-size:12px;color:var(--ink-soft)">${esc(priceHint)}</div>
        </button>
      `;
    }

    function pickOne(productId) {
      const p = products.find((x) => x.id === productId);
      if (!p) return;
      // Step 2: capture qty + dimensions (for ordering, NOT pricing) + room
      // Window-like products get dimension fields; flat services don't.
      const isPhysical = !["install", "repair"].includes(p.category);
      bg.querySelector(".modal-body").innerHTML = `
        <div style="padding:22px">
          <div style="margin-bottom:14px">
            <div style="font-size:11px;letter-spacing:0.1em;text-transform:uppercase;color:var(--ink-muted);font-weight:600">${esc(p.category)}</div>
            <div style="font-size:16px;font-weight:600;color:var(--ink);margin-top:2px">${esc(p.name)}</div>
            <div style="font-size:12px;color:var(--ink-soft);margin-top:2px">
              Unit price: <strong>${fmtMoney(p.base_price_cents)}</strong> per ${esc(p.unit || "ea")}
            </div>
          </div>
          <div class="form">
            <div class="row">
              <label><span>Qty</span><input id="pp-qty" type="number" min="1" step="1" value="1" required/></label>
              <label><span>Room (optional)</span><input id="pp-room" placeholder="Living, Primary BR…"/></label>
            </div>
            ${isPhysical ? `
              <div class="row">
                <label><span>Color / Finish</span><input id="pp-color" placeholder="White, walnut, espresso…"/></label>
                <label><span>Options</span><input id="pp-options" placeholder="Cordless, motorized, blackout…"/></label>
              </div>
              <div class="row">
                <label><span>Width (in) — for ordering</span><input id="pp-w" type="number" min="0" step="0.125" placeholder="e.g. 36"/></label>
                <label><span>Height (in) — for ordering</span><input id="pp-h" type="number" min="0" step="0.125" placeholder="e.g. 60"/></label>
              </div>
              <p style="font-size:11px;color:var(--ink-muted);margin:-4px 0 0">All of these are editable on the line later — set defaults here.</p>
            ` : ""}
            <div id="pp-preview" style="background:var(--bg-soft);padding:12px 16px;border-radius:var(--r-sm);font-size:13px;color:var(--ink-soft);font-variant-numeric:tabular-nums">
              <div>Unit price: <strong>${fmtMoney(p.base_price_cents)}</strong></div>
              <div>Line total: <strong id="pp-total" style="color:var(--money)">${fmtMoney(p.base_price_cents)}</strong></div>
            </div>
          </div>
        </div>
      `;
      bg.querySelector(".modal-foot").innerHTML = `
        <button class="btn ghost" id="pp-back">← Back</button>
        <button class="btn primary" id="pp-add">Add to line items</button>
      `;
      const qty = bg.querySelector("#pp-qty");
      const room = bg.querySelector("#pp-room");
      const w = bg.querySelector("#pp-w");
      const h = bg.querySelector("#pp-h");
      const unit = p.base_price_cents || 0;

      function recalc() {
        const qtyVal = Math.max(1, Math.round(Number(qty.value || 1)));
        const total = qtyVal * unit;
        bg.querySelector("#pp-total").textContent = fmtMoney(total);
        bg.dataset.unit = unit;
        bg.dataset.total = total;
      }
      qty.addEventListener("input", recalc);
      recalc();
      // Default focus to qty (then tab through to dimensions)
      qty.focus(); qty.select();

      bg.querySelector("#pp-back").onclick = () => {
        bg.querySelector(".modal-body").innerHTML = `
          <div style="padding:14px 22px;border-bottom:1px solid var(--line-soft);display:flex;gap:10px;align-items:center;flex-wrap:wrap"></div>
          <div id="pp-list" style="max-height:420px;overflow-y:auto"></div>
        `;
        bg.querySelector(".modal-foot").innerHTML = `
          <button class="btn ghost" data-cancel>Cancel</button>
          <a class="btn ghost" href="/crm/products.html" target="_blank">Edit catalog →</a>
        `;
        bg.querySelector("[data-cancel]").onclick = () => close(null);
        // Re-mount the search controls
        bg.querySelector(".modal-body > div:first-child").innerHTML = `
          <input type="search" id="pp-q" placeholder="Search by product name or SKU…" autofocus
                 style="flex:1;min-width:200px;padding:8px 12px;border:1px solid var(--line-strong);border-radius:var(--r-sm);font-size:13px"/>
          <select id="pp-cat" style="padding:8px 10px;border:1px solid var(--line-strong);border-radius:var(--r-sm);font-size:13px">
            <option value="">All categories</option>
            ${CATEGORY_GROUPS.map((c) => `<option value="${c.key}">${esc(c.label)}</option>`).join("")}
          </select>
        `;
        // Re-bind to the new elements
        const nq = bg.querySelector("#pp-q");
        const nc = bg.querySelector("#pp-cat");
        nq.value = q.value;
        nc.value = cat.value;
        bg.querySelector("#pp-list").parentElement.appendChild(bg.querySelector("#pp-list"));
        // Re-bind list refs and re-render
        nq.addEventListener("input", () => { q.value = nq.value; q.dispatchEvent(new Event("input")); });
        nc.addEventListener("change", () => { cat.value = nc.value; cat.dispatchEvent(new Event("change")); });
        render();
      };

      bg.querySelector("#pp-add").onclick = () => {
        const qtyVal = Math.max(1, Math.round(Number(qty.value || 1)));
        const total = qtyVal * unit;
        const wv = w ? Number(w.value || 0) : 0;
        const hv = h ? Number(h.value || 0) : 0;
        const colorInput = bg.querySelector("#pp-color");
        const optionsInput = bg.querySelector("#pp-options");
        close({
          product_id: p.id,
          description: p.name,
          room: room.value.trim() || null,
          quantity: qtyVal,
          width_in: wv > 0 ? wv : null,
          height_in: hv > 0 ? hv : null,
          color: colorInput?.value.trim() || null,
          options: optionsInput?.value.trim() || null,
          unit_price_cents: unit,
          line_total_cents: total,
        });
      };
    }

    q.addEventListener("input", render);
    cat.addEventListener("change", render);
    render();
  });
}

window.SSCrm = {
  fetchJSON, mount, fmtMoney, fmtMoneyShort, parseMoney, fmtDate, fmtDateTime, fmtTime, esc, pill, logout, toast, confirmDialog,
  pickContact, pickJob, openModal, pickProduct,
  quickAddContact, quickAddJob, quickAddAppointment, quickAddEstimate, quickAddProposal, quickAddContract,
  PROJECT_STATUSES,
};
