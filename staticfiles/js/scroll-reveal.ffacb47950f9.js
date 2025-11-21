// Scroll Reveal Animations
if (typeof ScrollReveal !== 'undefined') {
    ScrollReveal({
        reset: false,
        distance: '80px',
        duration: 2000,
        delay: 200
    });

    // Home section animations
    ScrollReveal().reveal('.home-text span, .home-text h1, .home-text h2, .home-text p, .btn-group', { 
        origin: 'left',
        interval: 200
    });
    
    ScrollReveal().reveal('.home-img', { origin: 'right' });
    
    // Stats animations
    ScrollReveal().reveal('.stat-box', { origin: 'bottom', interval: 100 });
    
    // Section titles
    ScrollReveal().reveal('.about-title, .heading', { origin: 'top' });
    
    // About section
    ScrollReveal().reveal('.about-img-wrapper', { origin: 'left' });
    ScrollReveal().reveal('.about-text', { origin: 'right' });
    
    // Services and Portfolio boxes
    ScrollReveal().reveal('.box', { origin: 'bottom', interval: 150 });
}
