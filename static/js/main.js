// =====================================================
//  main.js  —  tema, menu mobile, header, reveal, contadores
// =====================================================

// --- Tema (persistente) ---
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;
try { if (localStorage.getItem('theme') === 'dark') body.classList.add('dark'); } catch (e) {}
if (themeToggle) {
  themeToggle.addEventListener('click', () => {
    body.classList.toggle('dark');
    try { localStorage.setItem('theme', body.classList.contains('dark') ? 'dark' : 'light'); } catch (e) {}
  });
}

// --- Menu mobile ---
const menuIcon = document.getElementById('menu-icon');
const navbar = document.querySelector('.navbar');
if (menuIcon && navbar) {
  menuIcon.addEventListener('click', () => navbar.classList.toggle('active'));
  document.querySelectorAll('.navbar a').forEach(l =>
    l.addEventListener('click', () => navbar.classList.remove('active'))
  );
}

// --- Header ao rolar ---
const header = document.querySelector('header');
if (header) {
  window.addEventListener('scroll', () =>
    header.classList.toggle('scrolled', window.scrollY > 20)
  );
}

// --- Reveal ao aparecer ---
const revIO = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('in'); revIO.unobserve(e.target); }
  });
}, { threshold: .14, rootMargin: '0px 0px -40px 0px' });
document.querySelectorAll('.reveal').forEach((el, i) => {
  el.style.transitionDelay = (i % 6 * 60) + 'ms';
  revIO.observe(el);
});

// --- Reveal ao aparecer ---
