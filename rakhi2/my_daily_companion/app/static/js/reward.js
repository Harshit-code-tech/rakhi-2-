// reward.js

document.addEventListener('DOMContentLoaded', () => {
    const achievementCards = document.querySelectorAll('.achievement-card');

    achievementCards.forEach(card => {
        card.addEventListener('click', () => {
            if (card.classList.contains('locked')) {
                alert('This achievement is still locked.');
            } else {
                alert('Congratulations! You unlocked this achievement.');
            }
        });
    });
});
