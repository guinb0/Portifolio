// Animação dos números das estatísticas
const animateNumbers = () => {
    const numbers = document.querySelectorAll('.stat-number');
    numbers.forEach(number => {
        const target = parseInt(number.textContent);
        let current = 0;
        const increment = target / 50;
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                number.textContent = target + (number.textContent.includes('+') ? '+' : '') + (number.textContent.includes('%') ? '%' : '');
                clearInterval(timer);
            } else {
                number.textContent = Math.floor(current);
            }
        }, 30);
    });
};

// Observer para animar quando a seção aparecer
const statsSection = document.querySelector('.stats');
if (statsSection) {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateNumbers();
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.5
    });
    observer.observe(statsSection);
}
