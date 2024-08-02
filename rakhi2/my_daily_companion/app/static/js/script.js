// script.js
// Main JavaScript file

document.addEventListener('DOMContentLoaded', function() {
    var myElement = document.getElementById('myElement');
    if (myElement) {
        myElement.addEventListener('click', function() {
            console.log('Element clicked');
        });
    }
});
