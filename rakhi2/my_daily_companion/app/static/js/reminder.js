document.addEventListener('DOMContentLoaded', function() {
    // Request notification permission
    if (Notification.permission !== 'granted') {
        Notification.requestPermission();
    }

    // Function to show notification
    function showNotification(title, body) {
        if (Notification.permission === 'granted') {
            new Notification(title, { body: body });
        }
    }

    // Schedule notifications for each reminder
    reminders.forEach(reminder => {
        const reminderTime = new Date(`${reminder.date}T${reminder.time}`);
        const now = new Date();
        const delay = reminderTime - now;

        if (delay > 0) {
            setTimeout(function() {
                showNotification('Reminder', `${reminder.title}: ${reminder.description}`);
            }, delay);
        }
    });
});