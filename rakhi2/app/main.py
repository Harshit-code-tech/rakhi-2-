import logging
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import os
import time
from datetime import datetime
from kivy.clock import Clock
from kivy.uix.popup import Popup

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load Kivy files
Builder.load_file(os.path.join('', 'templates', 'home_screen.kv'))
Builder.load_file(os.path.join('', 'templates', 'mood_tracker_screen.kv'))
Builder.load_file(os.path.join('', 'templates', 'habit_tracker_screen.kv'))
Builder.load_file(os.path.join('', 'templates', 'historical_data_screen.kv'))
Builder.load_file(os.path.join('', 'templates', 'rewards_screen.kv'))
Builder.load_file(os.path.join('', 'templates', 'settings_screen.kv'))

# Utility functions
def read_file(filename):
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return f.read().splitlines()
        return []
    except Exception as e:
        logging.error(f"Error reading file {filename}: {e}")
        return []

def write_file(filename, data):
    try:
        with open(filename, 'w') as f:
            for item in data:
                f.write(f"{item}\n")
    except Exception as e:
        logging.error(f"Error writing file {filename}: {e}")

class HomeScreen(Screen):
    pass

class HistoricalDataScreen(Screen):
    def on_pre_enter(self):
        try:
            self.load_data()
        except Exception as e:
            logging.error(f"Error in on_pre_enter: {e}")

    def load_data(self):
        try:
            moods = read_file('../moods.txt')
            habits = read_file('../habits.txt')
            self.display_data(moods, habits)
        except Exception as e:
            logging.error(f"Error in load_data: {e}")

    def display_data(self, moods, habits):
        try:
            self.ids.moods_list.clear_widgets()
            self.ids.habits_list.clear_widgets()
            for mood in moods:
                self.ids.moods_list.add_widget(Label(text=mood))
            for habit in habits:
                self.ids.habits_list.add_widget(Label(text=habit))
        except KeyError as e:
            logging.error(f"KeyError in display_data: {e}")
        except Exception as e:
            logging.error(f"Error in display_data: {e}")

class MoodTrackerScreen(Screen):
    def submit_mood(self, mood):
        logging.info(f"Mood submitted: {mood}")
        try:
            write_file('../moods.txt', read_file('moods.txt') + [mood])
            self.ids.mood_input.text = ''
            self.load_moods()
        except Exception as e:
            logging.error(f"Error in submit_mood: {e}")

    def delete_mood(self, mood):
        try:
            moods = read_file('../moods.txt')
            if mood in moods:
                moods.remove(mood)
                write_file('../moods.txt', moods)
                self.load_moods()
        except Exception as e:
            logging.error(f"Error deleting mood: {e}")

    def on_pre_enter(self):
        try:
            self.load_moods()
        except Exception as e:
            logging.error(f"Error in on_pre_enter: {e}")

    def load_moods(self):
        try:
            moods = read_file('../moods.txt')
            self.display_moods(moods)
        except Exception as e:
            logging.error(f"Error in load_moods: {e}")

    def display_moods(self, moods):
        try:
            self.ids.moods_list.clear_widgets()
            for mood in moods:
                box = BoxLayout(orientation='horizontal')
                box.add_widget(Label(text=mood))
                btn = Button(text='Delete', size_hint_x=0.2)
                btn.bind(on_release=lambda btn, mood=mood: self.delete_mood(mood))
                box.add_widget(btn)
                self.ids.moods_list.add_widget(box)
        except KeyError as e:
            logging.error(f"KeyError in display_moods: {e}")
        except Exception as e:
            logging.error(f"Error in display_moods: {e}")

class HabitTrackerScreen(Screen):
    def submit_habit(self, habit):
        logging.info(f"Habit submitted: {habit}")
        try:
            write_file('../habits.txt', read_file('habits.txt') + [habit])
            self.ids.habit_input.text = ''
            self.load_habits()
        except Exception as e:
            logging.error(f"Error in submit_habit: {e}")

    def delete_habit(self, habit):
        try:
            habits = read_file('../habits.txt')
            if habit in habits:
                habits.remove(habit)
                write_file('../habits.txt', habits)
                self.load_habits()
        except Exception as e:
            logging.error(f"Error deleting habit: {e}")

    def on_pre_enter(self):
        try:
            self.load_habits()
        except Exception as e:
            logging.error(f"Error in on_pre_enter: {e}")

    def load_habits(self):
        try:
            habits = read_file('../habits.txt')
            self.display_habits(habits)
        except Exception as e:
            logging.error(f"Error in load_habits: {e}")

    def display_habits(self, habits):
        try:
            self.ids.habits_list.clear_widgets()
            for habit in habits:
                box = BoxLayout(orientation='horizontal')
                box.add_widget(Label(text=habit))
                btn = Button(text='Delete', size_hint_x=0.2)
                btn.bind(on_release=lambda btn, habit=habit: self.delete_habit(habit))
                box.add_widget(btn)
                self.ids.habits_list.add_widget(box)
        except KeyError as e:
            logging.error(f"KeyError in display_habits: {e}")
        except Exception as e:
            logging.error(f"Error in display_habits: {e}")

class RewardsScreen(Screen):
    def on_pre_enter(self):
        try:
            self.display_rewards()
        except Exception as e:
            logging.error(f"Error in on_pre_enter: {e}")

    def display_rewards(self):
        try:
            moods = read_file('../moods.txt')
            habits = read_file('../habits.txt')

            mood_count = len(moods)
            habit_count = len(habits)

            self.ids.mood_rewards.text = f"Total Moods Tracked: {mood_count}"
            self.ids.habit_rewards.text = f"Total Habits Tracked: {habit_count}"

            reward_message = self.calculate_rewards(mood_count, habit_count)
            self.ids.reward_message.text = reward_message
        except KeyError as e:
            logging.error(f"KeyError in display_rewards: {e}")
        except Exception as e:
            logging.error(f"Error in display_rewards: {e}")

    def calculate_rewards(self, mood_count, habit_count):
        try:
            if mood_count >= 10 and habit_count >= 10:
                return "Congratulations! You've earned a gold reward!"
            elif mood_count >= 5 and habit_count >= 5:
                return "Great job! You've earned a silver reward!"
            elif mood_count >= 1 and habit_count >= 1:
                return "Good start! You've earned a bronze reward!"
            else:
                return "Keep tracking your moods and habits to earn rewards!"
        except Exception as e:
            logging.error(f"Error in calculate_rewards: {e}")
            return "Error in calculating rewards."

class SettingsScreen(Screen):
    def set_reminder(self):
        reminder_time = self.ids.reminder_time_input.text
        logging.info(f"Reminder set for {reminder_time}")
        try:
            self.schedule_reminder(reminder_time)
            self.ids.reminder_message.text = f"Reminder set for {reminder_time}"
        except Exception as e:
            logging.error(f"Error in set_reminder: {e}")
            self.ids.reminder_message.text = "Error setting reminder"

    def schedule_reminder(self, reminder_time):
        try:
            now = datetime.now()
            reminder_dt = datetime.strptime(reminder_time, '%H:%M').replace(year=now.year, month=now.month, day=now.day)

            if reminder_dt < now:
                reminder_dt = reminder_dt.replace(day=now.day + 1)

            delay = (reminder_dt - now).total_seconds()
            Clock.schedule_once(self.show_reminder, delay)
        except ValueError as e:
            logging.error(f"ValueError in schedule_reminder: {e}")
        except Exception as e:
            logging.error(f"Error in schedule_reminder: {e}")

    def show_reminder(self, dt):
        try:
            popup = Popup(title='Reminder', content=Label(text='Time to check your moods and habits!'), size_hint=(0.6, 0.4))
            popup.open()
        except Exception as e:
            logging.error(f"Error in show_reminder: {e}")

class MyDailyCompanionApp(App):
    def build(self):
        try:
            sm = ScreenManager()
            sm.add_widget(HomeScreen(name='home'))
            sm.add_widget(MoodTrackerScreen(name='mood_tracker'))
            sm.add_widget(HabitTrackerScreen(name='habit_tracker'))
            sm.add_widget(HistoricalDataScreen(name='historical_data'))
            sm.add_widget(RewardsScreen(name='rewards'))
            sm.add_widget(SettingsScreen(name='settings'))
            return sm
        except Exception as e:
            logging.error(f"Error in build: {e}")

if __name__ == '__main__':
    try:
        MyDailyCompanionApp().run()
    except Exception as e:
        logging.error(f"Error running app: {e}")
