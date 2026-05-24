// Stately Shades — small enhancements
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

  // Graceful image fallback: if a content image fails, swap to brand placeholder
  document.querySelectorAll('img').forEach(img => {
    img.addEventListener('error', () => {
      if (img.dataset.fallback === 'true') return;
      img.dataset.fallback = 'true';
      img.src = '/assets/images/placeholder.svg';
    }, { once: true });
  });
})();
