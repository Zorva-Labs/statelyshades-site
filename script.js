// Stately Shades — editorial enhancements
(() => {
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

  // Scroll reveal — staggered editorial cascade via IntersectionObserver
  const prefersReduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!prefersReduce && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const targets = entry.target.querySelectorAll('[data-reveal]');
        const list = targets.length ? Array.from(targets) : [entry.target];
        list.forEach((el, i) => {
          el.style.setProperty('--reveal-delay', `${i * 90}ms`);
          el.classList.add('is-visible');
        });
        observer.unobserve(entry.target);
      });
    }, { root: null, rootMargin: '0px 0px -8% 0px', threshold: 0.12 });

    document.querySelectorAll('[data-reveal-group]').forEach((g) => io.observe(g));
    document.querySelectorAll('[data-reveal]:not([data-reveal-group] [data-reveal])').forEach((el) => {
      const wrapper = document.createElement('span');
      // simple individual observer
      const indiv = new IntersectionObserver((entries, ob) => {
        entries.forEach(e => {
          if (e.isIntersecting) { e.target.classList.add('is-visible'); ob.unobserve(e.target); }
        });
      }, { threshold: 0.15, rootMargin: '0px 0px -6% 0px' });
      indiv.observe(el);
    });
  } else {
    document.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('is-visible'));
  }

  // Graceful image fallback: if a content image fails, swap to brand placeholder
  document.querySelectorAll('img').forEach(img => {
    img.addEventListener('error', () => {
      if (img.dataset.fallback === 'true') return;
      img.dataset.fallback = 'true';
      img.src = '/assets/images/placeholder.svg';
    }, { once: true });
  });
})();
