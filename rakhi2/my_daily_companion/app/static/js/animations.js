// animations.js
// JavaScript file for custom animations

document.addEventListener('DOMContentLoaded', function() {
    var elements = document.querySelectorAll('.fade-in');
    elements.forEach(function(element) {
        element.style.opacity = 0;
        element.style.transition = 'opacity 2s ease-in';
        element.style.opacity = 1;
    });

    var navbarToggler = document.querySelector('.navbar-toggler');
    var navbarCollapse = document.querySelector('.navbar-collapse');

    navbarToggler.addEventListener('click', function() {
        this.classList.toggle('active');
        navbarCollapse.classList.toggle('active');
    });
});
