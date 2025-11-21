// Theme Toggle Functionality
const themeToggle = document.getElementById('theme-toggle');
const navbarThemeToggle = document.getElementById('navbar-theme-toggle');
const htmlElement = document.documentElement;

// Função para aplicar tema
function applyTheme(theme) {
    if (theme === 'dark') {
        htmlElement.setAttribute('data-theme', 'dark');
    } else {
        htmlElement.removeAttribute('data-theme');
    }
}

// Carregar tema salvo
window.addEventListener('load', () => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    applyTheme(savedTheme);
});

// Função para alternar tema
function toggleTheme() {
    const currentTheme = htmlElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    applyTheme(newTheme);
    localStorage.setItem('theme', newTheme);
}

// Toggle tema desktop/tablet
if (themeToggle) {
    themeToggle.addEventListener('click', toggleTheme);
}

// Toggle tema mobile (navbar)
if (navbarThemeToggle) {
    navbarThemeToggle.addEventListener('click', toggleTheme);
}
