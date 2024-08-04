// static/js/mood_slider.js
// Mood intensity slider with description
document.addEventListener('DOMContentLoaded', function() {
    const intensitySlider = document.getElementById('intensity-slider');
    const intensityBox = document.getElementById('intensity-box');

    if (intensitySlider && intensityBox) {
        function updateIntensity() {
            const value = parseFloat(intensitySlider.value);
            let description = '';
            if (value >= 0 && value < 1) {
                description = 'Very Low';
            } else if (value >= 1 && value < 2) {
                description = 'Low';
            } else if (value >= 2 && value < 3) {
                description = 'Moderate';
            } else if (value >= 3 && value < 4) {
                description = 'High';
            } else if (value >= 4 && value <= 5) {
                description = 'Very High';
            }
            intensityBox.value = description + ' (' + value.toFixed(1) + ')';
            intensitySlider.setAttribute('value', value.toFixed(1));
        }

        intensitySlider.addEventListener('input', updateIntensity);
        updateIntensity(); // Initial call to set the box value on page load
    }
});
