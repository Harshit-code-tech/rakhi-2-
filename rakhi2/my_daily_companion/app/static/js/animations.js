// animations.js
// JavaScript file for custom animations

function fadeInElement(element) {
    element.classList.add('fade-in');
}

// Example usage
window.onload = function () {
    const element = document.getElementById('fade-in-target');
    fadeInElement(element);
};
