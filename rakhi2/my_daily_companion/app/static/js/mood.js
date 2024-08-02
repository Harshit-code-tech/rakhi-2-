// mood.js
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');
    const hintIcon = document.querySelector('.hint-icon');
    const hintText = document.querySelector('.hint-text');

    if (hintIcon && hintText) {
        console.log('Hint elements found');
        hintIcon.addEventListener('mouseenter', function() {
            console.log('Mouse entered hint icon');
            hintText.style.visibility = 'visible';
        });

        hintIcon.addEventListener('mouseleave', function() {
            console.log('Mouse left hint icon');
            hintText.style.visibility = 'hidden';
        });
    } else {
        console.log('Hint elements not found');
    }
});
