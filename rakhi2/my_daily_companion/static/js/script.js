document.addEventListener('DOMContentLoaded', function () {

    // Home functionality
    const animatedBox = document.querySelector('.animated-box');
    animatedBox.addEventListener('mouseenter', () => {
        animatedBox.style.animation = 'bounce 1s ease-in-out';
    });
    animatedBox.addEventListener('animationend', () => {
        animatedBox.style.animation = '';
    });
    // Habit Tracker functionality
    const habitTracker = document.getElementById('habit-tracker');
    if (habitTracker) {
        const addHabitButton = document.getElementById('add-habit-button');
        const habitList = document.querySelector('.habit-list');
        if (addHabitButton) {
            addHabitButton.addEventListener('click', function () {
                const newHabit = document.createElement('div');
                newHabit.className = 'habit';
                newHabit.innerText = 'New Habit';
                habitList.appendChild(newHabit);
            });
        }
    }

    // Mood Tracker functionality
    const moodTracker = document.getElementById('mood-tracker');
    if (moodTracker) {
        const addMoodButton = document.getElementById('add-mood-button');
        const moodList = document.querySelector('.mood-list');
        if (addMoodButton) {
            addMoodButton.addEventListener('click', function () {
                const newMood = document.createElement('div');
                newMood.className = 'mood';
                newMood.innerText = 'New Mood';
                moodList.appendChild(newMood);
            });
        }
    }

    // Historical Data functionality
    const historicalData = document.getElementById('historical-data');
    if (historicalData) {
        const ctx = document.getElementById('historical-data-chart').getContext('2d');
        // Example: Create a chart using Chart.js or any other chart library
        const chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
                datasets: [{
                    label: 'Sample Data',
                    data: [65, 59, 80, 81, 56, 55, 40],
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Rewards functionality
    const rewards = document.getElementById('rewards');
    if (rewards) {
        const rewardList = document.querySelector('.reward-list');
        // Example: Add rewards functionality here
    }

    // Settings functionality
    const settings = document.getElementById('settings');
    if (settings) {
        const settingsForm = document.getElementById('settings-form');
        // Example: Add settings form submission functionality here
    }

    // Reminder functionality
    const reminder = document.getElementById('reminder');
    if (reminder) {
        const addReminderButton = document.getElementById('add-reminder-button');
        const reminderList = document.querySelector('.reminder-list');
        if (addReminderButton) {
            addReminderButton.addEventListener('click', function () {
                const newReminder = document.createElement('div');
                newReminder.className = 'reminder';
                newReminder.innerText = 'New Reminder';
                reminderList.appendChild(newReminder);
            });
        }
    }
});
