// Menu Mobile
const menuIcon = document.getElementById('menu-icon');
const navbar = document.querySelector('.navbar');

if (menuIcon && navbar) {
    menuIcon.addEventListener('click', () => {
        navbar.classList.toggle('active');
    });

    // Fechar menu ao clicar em um link
    document.querySelectorAll('.navbar a').forEach(link => {
        link.addEventListener('click', () => {
            navbar.classList.remove('active');
        });
    });

    // Fechar menu ao clicar fora
    document.addEventListener('click', (e) => {
        if (!menuIcon.contains(e.target) && !navbar.contains(e.target)) {
            navbar.classList.remove('active');
        }
    });
}
