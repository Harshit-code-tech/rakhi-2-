// static/js/mood_intensity_slider.js
document.addEventListener('DOMContentLoaded', function() {
    const intensitySlider = document.getElementById('intensity-slider');
    const intensityValue = document.getElementById('intensity-value');
    if (intensitySlider && intensityValue) {
        intensitySlider.addEventListener('input', function() {
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
            intensityValue.textContent = description + ' (' + value.toFixed(1) + ')';
        });
    }
});
