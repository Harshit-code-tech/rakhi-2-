// static/js/mood.js
document.addEventListener('DOMContentLoaded', function() {
    const hintButton = document.getElementById('hint-button');
    const hintText = document.getElementById('hint-text');

    if (hintButton && hintText) {
        hintButton.addEventListener('click', function() {
            hintText.textContent = "Rate your day from 1 to 10. 0: Worse, 5: Neutral, 10: Best";
        });
    }
});