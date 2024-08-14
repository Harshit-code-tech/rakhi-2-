// app/static/js/animations.js
// JavaScript file for custom animations

document.addEventListener('DOMContentLoaded', function() {
    var anotherElement = document.getElementById('anotherElement');
    if (anotherElement) {
        anotherElement.addEventListener('mouseover', function() {
            console.log('Element hovered');
    });

    var navbarToggler = document.querySelector('.navbar-toggler');
    var navbarCollapse = document.querySelector('.navbar-collapse');

    navbarToggler.addEventListener('click', function() {
        this.classList.toggle('active');
        navbarCollapse.classList.toggle('active');
    });
}});
