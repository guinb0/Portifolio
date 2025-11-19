// Espera o DOM carregar completamente
document.addEventListener('DOMContentLoaded', function() {
    console.log('=== MENU.JS CARREGADO ===');
    
    // ===== MENU TOGGLE =====
    const menuIcon = document.getElementById('menu-icon');
    const navbar = document.getElementById('navbar');
    const menuOverlay = document.getElementById('menu-overlay');
    const navbarClose = document.getElementById('navbar-close');
    const navbarLinks = document.querySelectorAll('.navbar-list a:not(.dropdown-btn)');

    // Debug: verificar se elementos foram encontrados
    console.log('Menu Icon:', menuIcon);
    console.log('Navbar:', navbar);
    console.log('Menu Overlay:', menuOverlay);
    console.log('Navbar Close:', navbarClose);

    // Abrir menu
    if (menuIcon) {
        menuIcon.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('=== MENU CLICADO! ===');
            
            navbar.classList.add('active');
            menuOverlay.classList.add('active');
            menuIcon.classList.add('active');
            document.body.style.overflow = 'hidden';
            
            console.log('Classes adicionadas:', {
                navbar: navbar.classList.contains('active'),
                overlay: menuOverlay.classList.contains('active'),
                icon: menuIcon.classList.contains('active')
            });
        });
    } else {
        console.error('ERRO: menu-icon não encontrado!');
    }

    // Função para fechar menu
    function closeMenu() {
        navbar.classList.remove('active');
        menuOverlay.classList.remove('active');
        menuIcon.classList.remove('active');
        document.body.style.overflow = '';
        console.log('Menu fechado');
    }

    // Fechar menu - botão X
    if (navbarClose) {
        navbarClose.addEventListener('click', function() {
            closeMenu();
        });
    }

    // Fechar menu - clique no overlay
    if (menuOverlay) {
        menuOverlay.addEventListener('click', function() {
            closeMenu();
        });
    }

    // Fechar menu ao clicar em qualquer link
    navbarLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            closeMenu();
        });
    });

    // ===== DROPDOWN TOGGLE =====
    const dropdown = document.querySelector('.dropdown');
    const dropdownBtn = document.querySelector('.dropdown-btn');

    if (dropdownBtn) {
        dropdownBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            dropdown.classList.toggle('active');
        });
    }

    // ===== THEME TOGGLE =====
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;

    // Verifica tema salvo
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'dark') {
        body.classList.add('dark');
    }

    // Toggle do tema
    if (themeToggle) {
        themeToggle.addEventListener('click', function(e) {
            e.stopPropagation();
            body.classList.toggle('dark');
            
            if (body.classList.contains('dark')) {
                localStorage.setItem('theme', 'dark');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    }

    // ===== FECHAR MENU COM ESC =====
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && navbar.classList.contains('active')) {
            closeMenu();
        }
    });
    
    console.log('=== MENU.JS INICIALIZADO ===');
});