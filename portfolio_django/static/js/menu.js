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

    // Toggle menu (abrir/fechar)
    if (menuIcon) {
        menuIcon.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('=== MENU CLICADO! ===');
            
            // Se já está aberto, fecha. Se está fechado, abre.
            if (navbar.classList.contains('active')) {
                closeMenu();
            } else {
                navbar.classList.add('active');
                menuOverlay.classList.add('active');
                menuIcon.classList.add('active');
                
                console.log('Menu aberto');
            }
        });
    } else {
        console.error('ERRO: menu-icon não encontrado!');
    }

    // Função para fechar menu
    function closeMenu() {
        navbar.classList.remove('active');
        menuOverlay.classList.remove('active');
        menuIcon.classList.remove('active');
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
    const html = document.documentElement;

    // Aplica tema salvo ao carregar a página
    const savedTheme = localStorage.getItem('theme') || 'light';
    if (savedTheme === 'dark') {
        html.setAttribute('data-theme', 'dark');
    } else {
        html.setAttribute('data-theme', 'light');
    }

    // Toggle do tema
    if (themeToggle) {
        themeToggle.addEventListener('click', function(e) {
            e.stopPropagation();
            e.preventDefault();
            
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            console.log('Tema alterado para:', newTheme);
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