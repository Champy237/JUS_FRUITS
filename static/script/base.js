



document.addEventListener("DOMContentLoaded", () => {
    const target = document.querySelector('.typing-text');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                target.classList.add('show'); // Démarre l'animation
                observer.disconnect(); // Arrête l'observation après l'animation
            }
        });
    });

    observer.observe(target);
});
