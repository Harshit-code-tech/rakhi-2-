import logging
from datetime import datetime
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
class SettingsScreen(Screen):
    def set_reminder(self):
        reminder_time = self.ids.reminder_time_input.text
        logging.info(f"Reminder set for {reminder_time}")
        try:
            reminder_time = datetime.strptime(reminder_time, "%H:%M")
            self.schedule_reminder(reminder_time)
        except ValueError:
            logging.error("Invalid time format. Please use HH:MM format.")
            self.show_popup("Error", "Invalid time format. Please use HH:MM format.")

    def schedule_reminder(self, reminder_time):
        now = datetime.now()
        reminder_time_today = reminder_time.replace(year=now.year, month=now.month, day=now.day)

        if reminder_time_today < now:
            reminder_time_today = reminder_time_today.replace(day=now.day + 1)

        time_to_reminder = (reminder_time_today - now).total_seconds()
        Clock.schedule_once(lambda dt: self.show_popup("Reminder", "It's time for your reminder!"), time_to_reminder)

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.8, 0.4))
        popup.open()
