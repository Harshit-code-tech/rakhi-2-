document.addEventListener('DOMContentLoaded', () => {
    const animatedBox = document.querySelector('.animated-box');
    animatedBox.addEventListener('mouseenter', () => {
        animatedBox.style.animation = 'bounce 1s ease-in-out';
    });
    animatedBox.addEventListener('animationend', () => {
        animatedBox.style.animation = '';
    });
});