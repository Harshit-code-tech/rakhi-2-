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

    // Function to check reminders
    function checkReminders() {
        const now = new Date();

        reminders.forEach(reminder => {
            const reminderTime = new Date(`${reminder.date}T${reminder.time}`);
            const delay = reminderTime - now;

            if (delay <= 0 && !reminder.notified) {
                showNotification('Reminder', `${reminder.title}: ${reminder.description}`);
                reminder.notified = true;
            }
        });
    }

    // Schedule initial notifications
    reminders.forEach(reminder => {
        const reminderTime = new Date(`${reminder.date}T${reminder.time}`);
        const now = new Date();
        const delay = reminderTime - now;

        if (delay > 0) {
            setTimeout(function() {
                showNotification('Reminder', `${reminder.title}: ${reminder.description}`);
                reminder.notified = true;
            }, delay);
        }
    });

    // Check reminders every minute
    setInterval(checkReminders, 60000);
});