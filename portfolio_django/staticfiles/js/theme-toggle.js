// Theme Toggle Functionality
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Carregar tema salvo
window.addEventListener('load', () => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    if (savedTheme === 'dark') {
        body.classList.add('dark');
    }
});

// Toggle tema
if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        body.classList.toggle('dark');
        const currentTheme = body.classList.contains('dark') ? 'dark' : 'light';
        localStorage.setItem('theme', currentTheme);
    });
}
