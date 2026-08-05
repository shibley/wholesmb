/* WholeSMB — Minimal JS */

// Mobile nav toggle
document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      links.classList.toggle('open');
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', !expanded);
    });
    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!e.target.closest('.nav') && links.classList.contains('open')) {
        links.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', (e) => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // Affiliate / outbound CTA click tracking (Vercel Analytics custom events).
  // Delegated so it covers CTAs added to any page without extra markup.
  document.addEventListener('click', (e) => {
    const link = e.target.closest('a[rel~="sponsored"], a[rel~="nofollow"][target="_blank"]');
    if (!link) return;
    let host = '';
    try { host = new URL(link.href, window.location.href).hostname.replace(/^www\./, ''); } catch (_) { return; }
    if (!host || host === window.location.hostname.replace(/^www\./, '')) return;
    const payload = {
      partner: host,
      page: window.location.pathname,
      label: (link.textContent || '').trim().slice(0, 60)
    };
    if (typeof window.va === 'function') {
      window.va('event', { name: 'affiliate_click', data: payload });
    } else {
      // Vercel Analytics queues calls made before the script loads.
      (window.vaq = window.vaq || []).push(['event', { name: 'affiliate_click', data: payload }]);
    }
  }, true);
});
