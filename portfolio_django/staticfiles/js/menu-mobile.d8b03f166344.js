// Menu Mobile Hamburguer
const menuIcon = document.getElementById('menu-icon');
const navbar = document.getElementById('navbar');
const navbarClose = document.getElementById('navbar-close');
const menuOverlay = document.getElementById('menu-overlay');
const dropdownBtns = document.querySelectorAll('.dropdown-btn');

// Abrir menu
if (menuIcon && navbar) {
    menuIcon.addEventListener('click', () => {
        navbar.classList.add('active');
        menuIcon.classList.add('active');
        menuOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
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
    navbar.classList.remove('active');
    menuIcon.classList.remove('active');
    menuOverlay.classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Fechar menu ao clicar em um link
document.querySelectorAll('.navbar-list > li > a').forEach(link => {
    link.addEventListener('click', (e) => {
        // Não fechar se for um link do dropdown
        if (!link.closest('.dropdown-content')) {
            closeMenu();
        }
    });
});

// Toggle dropdown no mobile
dropdownBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const dropdown = btn.closest('.dropdown');
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
    if (e.key === 'Escape' && navbar.classList.contains('active')) {
        closeMenu();
    }
});
