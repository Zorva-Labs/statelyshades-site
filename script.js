// Stately Shades — editorial enhancements
(() => {
  // Venetian-blinds intro: play once per browser session, then keep the
  // overlay hidden so subsequent anchor jumps don't re-trigger it.
  // The CSS animation runs on its own; JS just cleans up + sessionStorage
  // remembers we've already shown it.
  const intro = document.querySelector('.slat-intro');
  if (intro) {
    if (sessionStorage.getItem('ss-intro-played') === '1') {
      intro.setAttribute('data-done', '');
    } else {
      sessionStorage.setItem('ss-intro-played', '1');
      setTimeout(() => { intro.setAttribute('data-done', ''); }, 1800);
    }
  }


  const nav = document.getElementById('nav');
  const toggle = document.querySelector('.nav__toggle');
  const links = document.querySelector('.nav__links');

  // Sticky nav scroll state
  const onScroll = () => {
    if (window.scrollY > 8) nav.classList.add('is-scrolled');
    else nav.classList.remove('is-scrolled');
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const open = links.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    links.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        links.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Year in footer
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  // Scroll reveal — opt-in via html.js class so the page is fully visible
  // if JS fails / is slow / disabled. Per-element observer with generous
  // rootMargin so the reveal fires well before the user can see the element,
  // never leaving a 'wall of cream' in any section.
  const prefersReduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if ('IntersectionObserver' in window && !prefersReduce) {
    document.documentElement.classList.add('js');

    const io = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      });
    }, {
      root: null,
      // 400px early-fire on both sides — element is revealed long before
      // the user scrolls into it, so even slow finger-scrolls never catch
      // a hidden block on screen.
      rootMargin: '400px 0px 400px 0px',
      threshold: 0,
    });

    document.querySelectorAll('[data-reveal]').forEach((el) => io.observe(el));

    // Stagger children of a [data-reveal-group] by 60ms apiece so the
    // sequence still feels orchestrated even with the early-fire window.
    document.querySelectorAll('[data-reveal-group]').forEach((g) => {
      const kids = g.querySelectorAll('[data-reveal]');
      kids.forEach((el, i) => {
        el.style.setProperty('--reveal-delay', `${i * 60}ms`);
      });
    });
  }
  // If JS doesn't run, html.js never gets added → CSS never hides anything →
  // content is fully visible. Same for prefers-reduced-motion users.

  // Graceful image fallback: if a content image fails, swap to brand placeholder
  document.querySelectorAll('img').forEach(img => {
    img.addEventListener('error', () => {
      if (img.dataset.fallback === 'true') return;
      img.dataset.fallback = 'true';
      img.src = '/assets/images/placeholder.svg';
    }, { once: true });
  });

  // ============================================================
  // Sitewide search — inject button into every nav, modal overlay
  // with live filter against /search-index.json. Runs on every page
  // because script.js is loaded sitewide.
  // ============================================================
  (function initSearch() {
    const navInner = document.querySelector('.nav .nav__inner');
    const navToggle = document.querySelector('.nav__toggle');
    if (!navInner || !navToggle) return;

    // ----- Inject the search button before the hamburger toggle -----
    const btn = document.createElement('button');
    btn.className = 'nav__search';
    btn.type = 'button';
    btn.setAttribute('aria-label', 'Search the site');
    btn.innerHTML =
      '<svg viewBox="0 0 24 24" aria-hidden="true">' +
      '<circle cx="11" cy="11" r="7"></circle>' +
      '<line x1="16.5" y1="16.5" x2="21" y2="21" stroke-linecap="round"></line>' +
      '</svg>';
    navInner.insertBefore(btn, navToggle);

    // ----- Build modal DOM once, append to body -----
    const modal = document.createElement('div');
    modal.className = 'search-modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-label', 'Search');
    modal.innerHTML =
      '<div class="search-modal__card">' +
        '<div class="search-modal__head">' +
          '<svg viewBox="0 0 24 24" aria-hidden="true">' +
            '<circle cx="11" cy="11" r="7"></circle>' +
            '<line x1="16.5" y1="16.5" x2="21" y2="21" stroke-linecap="round"></line>' +
          '</svg>' +
          '<input type="search" class="search-modal__input" ' +
            'placeholder="Search guides, products, services…" ' +
            'autocomplete="off" autocapitalize="off" spellcheck="false" />' +
          '<button class="search-modal__close" type="button" aria-label="Close search">Esc</button>' +
        '</div>' +
        '<ul class="search-modal__results" role="listbox"></ul>' +
        '<div class="search-modal__footer">' +
          'Type to search · ' +
          '<kbd>↑</kbd><kbd>↓</kbd> navigate · ' +
          '<kbd>Enter</kbd> open · ' +
          '<kbd>Esc</kbd> close' +
        '</div>' +
      '</div>';
    document.body.appendChild(modal);

    const input = modal.querySelector('.search-modal__input');
    const resultsEl = modal.querySelector('.search-modal__results');
    const closeBtn = modal.querySelector('.search-modal__close');

    let indexCache = null;
    let activeIdx = -1;
    let lastResults = [];

    // ----- Fetch the index (once, on first open) -----
    async function loadIndex() {
      if (indexCache) return indexCache;
      try {
        const res = await fetch('/search-index.json', { credentials: 'same-origin' });
        const data = await res.json();
        indexCache = (data && data.items) || [];
      } catch (e) {
        indexCache = [];
      }
      return indexCache;
    }

    // ----- Open / close -----
    async function open() {
      modal.setAttribute('data-open', 'true');
      document.body.setAttribute('data-search-open', 'true');
      await loadIndex();
      input.value = '';
      runQuery('');
      // Focus on the next tick so the animation doesn't fight us
      setTimeout(() => input.focus(), 30);
    }

    function close() {
      modal.removeAttribute('data-open');
      document.body.removeAttribute('data-search-open');
      activeIdx = -1;
    }

    // ----- Query / ranking -----
    function runQuery(rawQ) {
      const q = (rawQ || '').toLowerCase().trim();
      const items = indexCache || [];

      let results;
      if (!q) {
        // Empty query: show curated default set
        results = items.slice(0, 8);
      } else {
        const tokens = q.split(/\s+/).filter(Boolean);
        results = items
          .map((it) => {
            const hay = (
              it.title + ' ' + it.excerpt + ' ' + (it.tags || []).join(' ')
            ).toLowerCase();
            let score = 0;
            for (const t of tokens) {
              if (it.title.toLowerCase().includes(t)) score += 5;
              if ((it.tags || []).some((tag) => tag.toLowerCase().includes(t))) score += 3;
              if (hay.includes(t)) score += 1;
            }
            return { it, score };
          })
          .filter((x) => x.score > 0)
          .sort((a, b) => b.score - a.score)
          .slice(0, 12)
          .map((x) => x.it);
      }

      lastResults = results;
      activeIdx = results.length ? 0 : -1;
      renderResults(results, q);
    }

    function highlight(text, q) {
      if (!q) return text;
      const tokens = q.split(/\s+/).filter((t) => t.length >= 2);
      if (!tokens.length) return text;
      // Escape regex special chars in tokens
      const escaped = tokens.map((t) => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
      const re = new RegExp('(' + escaped.join('|') + ')', 'gi');
      return text.replace(re, '<mark>$1</mark>');
    }

    function renderResults(results, q) {
      if (!results.length) {
        resultsEl.innerHTML =
          '<li class="search-modal__empty">No matches. Try a product, room, or city.</li>';
        return;
      }
      const html = results
        .map((r, i) =>
          '<li role="option" aria-selected="' + (i === activeIdx ? 'true' : 'false') + '">' +
            '<a class="search-modal__result" href="' + r.url + '" data-idx="' + i + '" ' +
              (i === activeIdx ? 'aria-selected="true"' : '') + '>' +
              '<span class="search-modal__result-section">' + r.section + '</span>' +
              '<h3 class="search-modal__result-title">' + highlight(r.title, q) + '</h3>' +
              '<p class="search-modal__result-excerpt">' + highlight(r.excerpt, q) + '</p>' +
            '</a>' +
          '</li>'
        )
        .join('');
      resultsEl.innerHTML = html;
    }

    function setActive(newIdx) {
      const links = resultsEl.querySelectorAll('.search-modal__result');
      if (!links.length) return;
      activeIdx = (newIdx + links.length) % links.length;
      links.forEach((a, i) => {
        a.setAttribute('aria-selected', i === activeIdx ? 'true' : 'false');
        a.parentElement.setAttribute('aria-selected', i === activeIdx ? 'true' : 'false');
        if (i === activeIdx) {
          a.scrollIntoView({ block: 'nearest' });
        }
      });
    }

    function openActive() {
      if (activeIdx < 0 || activeIdx >= lastResults.length) return;
      window.location.href = lastResults[activeIdx].url;
    }

    // ----- Event wiring -----
    btn.addEventListener('click', open);
    closeBtn.addEventListener('click', close);

    modal.addEventListener('click', (e) => {
      // Click on backdrop (not on card) closes
      if (e.target === modal) close();
    });

    input.addEventListener('input', (e) => runQuery(e.target.value));

    input.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowDown') { e.preventDefault(); setActive(activeIdx + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(activeIdx - 1); }
      else if (e.key === 'Enter') { e.preventDefault(); openActive(); }
      else if (e.key === 'Escape') { close(); }
    });

    // Global '/' shortcut opens search (unless typing in an input)
    document.addEventListener('keydown', (e) => {
      if (e.key === '/' && !modal.getAttribute('data-open')) {
        const tag = (document.activeElement && document.activeElement.tagName) || '';
        if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;
        e.preventDefault();
        open();
      } else if (e.key === 'Escape' && modal.getAttribute('data-open')) {
        close();
      }
    });
  })();

  // Contact forms: POST to /api/contact (saves to CRM + sends Purelymail email).
  // All <form class="form"> elements wire up the same way. Each carries a
  // data-form-source attribute so we can tell which form fired the lead.
  document.querySelectorAll('form.form').forEach((form) => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = form.querySelector('button[type="submit"]');
      const originalLabel = btn ? btn.innerHTML : '';
      const isCompact = form.classList.contains('form--compact');
      const source = form.dataset.formSource || 'unknown';

      const setBusy = (busy) => {
        if (!btn) return;
        btn.disabled = busy;
        btn.innerHTML = busy ? 'Sending&hellip;' : originalLabel;
      };

      // Clear any previous error
      form.querySelectorAll('.form__error').forEach(n => n.remove());

      setBusy(true);
      const data = Object.fromEntries(new FormData(form).entries());
      data.source = source;

      try {
        const res = await fetch(form.action, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify(data),
        });
        const body = await res.json().catch(() => ({}));
        if (!res.ok || body.error) throw new Error(body.error || 'Network error');

        const success = document.createElement('div');
        success.className = isCompact ? 'form__success form__success--light' : 'form form__success';
        success.innerHTML = isCompact
          ? `
            <span class="eyebrow" style="color: var(--color-brass-hot);">Thank You</span>
            <h3 style="font-family: var(--font-display); font-size: clamp(1.5rem, 2.2vw, 2rem); font-weight: 400; color: var(--color-bg); margin: 6px 0 12px;">Request sent.</h3>
            <p style="color: rgba(247, 242, 234, 0.82); font-family: var(--font-display); font-style: italic; font-size: 1.05rem; line-height: 1.55; margin: 0;">We'll be in touch within one business day to schedule your free in-home consultation. For anything urgent, call <a href="tel:+16292988241" style="color: var(--color-bg); border-bottom: 1px solid var(--color-brass-hot);">629-298-8241</a>.</p>
          `
          : `
            <span class="eyebrow eyebrow--light">Thank You</span>
            <h3 style="font-family: var(--font-display); font-size: clamp(1.6rem, 2.3vw, 2.1rem); font-weight: 400; color: var(--color-bg); margin: 8px 0 14px;">Your request has been sent.</h3>
            <p style="color: rgba(247,242,234,.82); font-family: var(--font-display); font-style: italic; font-size: 1.08rem; line-height: 1.55; margin: 0;">We'll be in touch within one business day to schedule your complimentary in-home consultation. For anything urgent, call or text <a href="tel:+16292988241" style="color: var(--color-champagne); border-bottom: 1px solid currentColor;">629-298-8241</a>.</p>
          `;
        form.replaceWith(success);
      } catch (err) {
        const errBox = document.createElement('p');
        errBox.className = 'form__error';
        errBox.style.cssText = (isCompact ? 'color: #B85450;' : 'color: #E89B7C;') + ' font-size: 0.9rem; margin: 0; text-align: center; font-family: var(--font-body);';
        errBox.textContent = err.message || 'Something went wrong. Please call us at 629-298-8241.';
        btn.parentNode.insertBefore(errBox, btn);
        setBusy(false);
      }
    });
  });
})();
