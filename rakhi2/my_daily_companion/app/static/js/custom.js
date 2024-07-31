$(document).ready(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('.navbar').addClass('scrolled');
        } else {
            $('.navbar').removeClass('scrolled');
        }
    });

    particlesJS.load('particles-js', '/static/js/particles.json', function() {
        console.log('particles.json loaded...');
    });
});
