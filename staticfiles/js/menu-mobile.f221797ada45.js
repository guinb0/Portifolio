// Menu Mobile Hamburguer
const menuIcon = document.getElementById('menu-icon');
const navbar = document.getElementById('navbar');
const navbarClose = document.getElementById('navbar-close');
const menuOverlay = document.getElementById('menu-overlay');
const dropdownBtns = document.querySelectorAll('.dropdown-btn');

// Abrir/Fechar menu (toggle)
if (menuIcon && navbar) {
    menuIcon.addEventListener('click', () => {
        const isActive = navbar.classList.contains('active');
        
        if (isActive) {
            // Se está aberto, fechar
            closeMenu();
        } else {
            // Se está fechado, abrir
            navbar.classList.add('active');
            menuIcon.classList.add('active');
            menuOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    });
}

// Fechar menu pelo X
if (navbarClose) {
    navbarClose.addEventListener('click', closeMenu);
}

// Fechar menu pelo overlay
if (menuOverlay) {
    menuOverlay.addEventListener('click', closeMenu);
}

// Função para fechar menu
function closeMenu() {
    if (navbar) navbar.classList.remove('active');
    if (menuIcon) menuIcon.classList.remove('active');
    if (menuOverlay) menuOverlay.classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Fechar menu ao clicar em um link (exceto dropdown)
document.querySelectorAll('.navbar-list > li > a:not(.dropdown-btn)').forEach(link => {
    link.addEventListener('click', () => {
        closeMenu();
    });
});

// Toggle dropdown no mobile
dropdownBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const dropdown = btn.closest('.dropdown');
        
        // Fechar outros dropdowns
        document.querySelectorAll('.dropdown').forEach(d => {
            if (d !== dropdown) {
                d.classList.remove('active');
            }
        });
        
        dropdown.classList.toggle('active');
    });
});

// Fechar dropdown ao clicar em uma opção
document.querySelectorAll('.dropdown-content a').forEach(link => {
    link.addEventListener('click', () => {
        closeMenu();
    });
});

// Fechar menu com ESC
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && navbar && navbar.classList.contains('active')) {
        closeMenu();
    }
});

// Header scroll effect
window.addEventListener('scroll', () => {
    const header = document.querySelector('.site-header');
    if (window.scrollY > 50) {
        header?.classList.add('scrolled');
    } else {
        header?.classList.remove('scrolled');
    }
});