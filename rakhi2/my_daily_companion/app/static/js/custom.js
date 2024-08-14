//app/static/js/custom.js
document.addEventListener('DOMContentLoaded', function() {
    if (typeof particlesJS !== 'undefined') {
        particlesJS.load('particles-js', '{% static "js/particles-config.json" %}', function() {
            console.log('callback - particles.js config loaded');
        });
    } else {
        console.error('particlesJS is not defined');
    }
});
