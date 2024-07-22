# main2.py
import kivy
kivy.require('2.0.0')
from kivy.config import Config
import logging
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import os
import time
from kivy.clock import Clock
from kivy.uix.popup import Popup
from datetime import datetime

# Importing authentication functions from logging_script.py
from logging_script import authenticate_user, register_user, read_file, write_file

# Configure logging
logging.basicConfig(level=logging.INFO, filename='data/log/app.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

# Function to clean up old logs
def cleanup_old_logs():
    try:
        log_dir = os.path.expanduser('~/.kivy/logs')
        log_files = sorted([f for f in os.listdir(log_dir) if f.startswith('kivy_')], reverse=True)
        for log_file in log_files[10:]:
            os.remove(os.path.join(log_dir, log_file))
            print(f"Deleted old log file: {log_file}")
    except Exception as e:
        logging.error(f"Error in cleanup_old_logs: {e}")

cleanup_old_logs()

# Load all KV files
kv_path = os.path.join(os.path.dirname(__file__), 'templates')
kv_files = [
    'home_screen.kv', 'mood_tracker_screen.kv', 'habit_tracker_screen.kv',
    'historical_data_screen.kv', 'rewards_screen.kv', 'reminder_screen.kv',
    'audio_mood_tracker_screen.kv', 'chat_room_screen.kv', 'auth_screen.kv'
]
for kv_file in kv_files:
    try:
        kv_file_path = os.path.join(kv_path, kv_file)
        Builder.load_file(kv_file_path)
        print(f"Loaded KV file: {kv_file_path}")
    except Exception as e:
        logging.error(f"Error loading KV file {kv_file}: {e}")


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
    def on_pre_enter(self, *args):
        # Check if the auth_screen exists
        auth_screen = self.manager.get_screen('auth_screen')
        if auth_screen:
            self.ids.username_label.text = f"Welcome, {auth_screen.ids.username.text}!"
        else:
            print("Error: auth_screen not found")


    def logout(self):
        self.manager.current = 'auth_screen'


class HistoricalDataScreen(Screen):
    def on_pre_enter(self):
        try:
            self.load_data()
        except Exception as e:
            logging.error(f"Error in on_pre_enter: {e}")

    def load_data(self):
        try:
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            moods = read_file(f'data/db/{user_id}/moods.txt')
            habits = read_file(f'data/db/{user_id}/habits.txt')
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
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            write_file(f'data/db/{user_id}/moods.txt', read_file(f'data/db/{user_id}/moods.txt') + [mood])
            self.ids.mood_input.text = ''
            self.load_moods()
        except Exception as e:
            logging.error(f"Error in submit_mood: {e}")

    def delete_mood(self, mood):
        try:
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            moods = read_file(f'data/db/{user_id}/moods.txt')
            if mood in moods:
                moods.remove(mood)
                write_file(f'data/db/{user_id}/moods.txt', moods)
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
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            moods = read_file(f'data/db/{user_id}/moods.txt')
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
            write_file('data/db/habits.txt', read_file('data/db/habits.txt') + [habit])
            self.ids.habit_input.text = ''
            self.load_habits()
        except Exception as e:
            logging.error(f"Error in submit_habit: {e}")

    def delete_habit(self, habit):
        try:
            habits = read_file('data/db/habits.txt')
            if habit in habits:
                habits.remove(habit)
                write_file('data/db/habits.txt', habits)
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
            habits = read_file('data/db/habits.txt')
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
            moods = read_file('data/db/moods.txt')
            habits = read_file('data/db/habits.txt')

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
            return "Error calculating rewards."

class AudioMoodTrackerScreen(Screen):
    def on_pre_enter(self):
        self.start_audio_processing()

    def start_audio_processing(self):
        # Code to start audio processing and mood detection
        pass

    def display_detected_mood(self, mood):
        self.ids.detected_mood_label.text = f"Detected Mood: {mood}"

class ChatRoomScreen(Screen):
    def on_pre_enter(self):
        self.ids.chat_log.text = ""

    def send_message(self):
        user_input = self.ids.user_input.text
        response = self.get_gpt2_response(user_input)
        self.ids.chat_log.text += f"User: {user_input}\nBot: {response}\n"
        self.ids.user_input.text = ""

    def get_gpt2_response(self, input_text):
        # Code to get response from Hugging Face GPT-2 model
        pass

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

class AuthScreen(Screen):
    def __init__(self, **kwargs):
        super(AuthScreen, self).__init__(**kwargs)
        self.authenticated = False

    def login(self):
        user_id = self.ids.username.text
        password = self.ids.password.text

        if authenticate_user(user_id, password):
            self.authenticated = True
            self.manager.current = 'home_screen'
        else:
            popup = Popup(title='Login Failed', content=Label(text='Invalid username or password'), size_hint=(0.6, 0.4))
            popup.open()

    def register(self):
        user_id = self.ids.username.text
        password = self.ids.password.text

        if register_user(user_id, password):
            popup = Popup(title='Registration Successful', content=Label(text='Registration successful! You can now log in.'), size_hint=(0.6, 0.4))
            popup.open()
        else:
            popup = Popup(title='Registration Failed', content=Label(text='User ID already exists'), size_hint=(0.6, 0.4))
            popup.open()


class MyDailyCompanionApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AuthScreen(name='auth_screen'))
        sm.add_widget(HomeScreen(name='home_screen'))
        sm.add_widget(HistoricalDataScreen(name='historical_data_screen'))
        sm.add_widget(MoodTrackerScreen(name='mood_tracker_screen'))
        sm.add_widget(HabitTrackerScreen(name='habit_tracker_screen'))
        sm.add_widget(RewardsScreen(name='rewards_screen'))
        sm.add_widget(AudioMoodTrackerScreen(name='audio_mood_tracker_screen'))
        sm.add_widget(ChatRoomScreen(name='chat_room_screen'))
        sm.add_widget(SettingsScreen(name='settings_screen'))

        return sm

if __name__ == '__main__':
    MyDailyCompanionApp().run()
