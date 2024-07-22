# main2.py
import logging
import os
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

from rakhi2.app.screens.home_screen import HomeScreen
from rakhi2.app.screens.mood_tracker_screen import MoodTrackerScreen
from rakhi2.app.screens.habit_tracker_screen import HabitTrackerScreen
from rakhi2.app.screens.historical_data_screen import HistoricalDataScreen
from rakhi2.app.screens.rewards_screen import RewardsScreen
from rakhi2.app.screens.reminder_screen import ReminderScreen
from rakhi2.app.screens.audio_mood_tracker_screen import AudioMoodTrackerScreen
from rakhi2.app.screens.chat_room_screen import ChatRoomScreen
from rakhi2.app.screens.auth_screen import AuthScreen
from rakhi2.app.logging_script import setup_logging

setup_logging()

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
        logging.info(f"Loaded KV file: {kv_file_path}")
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

def cleanup_old_logs():
    try:
        log_dir = os.path.expanduser('~/.kivy/logs')
        if os.path.exists(log_dir):
            log_files = sorted([f for f in os.listdir(log_dir) if f.startswith('kivy_')], reverse=True)
            for log_file in log_files[10:]:
                os.remove(os.path.join(log_dir, log_file))
                logging.info(f"Deleted old log file: {log_file}")
    except Exception as e:
        logging.error(f"Error in cleanup_old_logs: {e}")

cleanup_old_logs()

class MyScreenManager2(ScreenManager):
    pass

class MyDailyCompanionApp2(App):
    def build(self):
        try:
            sm = MyScreenManager2()
            sm.add_widget(AuthScreen(name='auth_screen'))
            sm.add_widget(HomeScreen(name='home_screen'))
            sm.add_widget(HistoricalDataScreen(name='historical_data_screen'))
            sm.add_widget(MoodTrackerScreen(name='mood_tracker_screen'))
            sm.add_widget(HabitTrackerScreen(name='habit_tracker_screen'))
            sm.add_widget(RewardsScreen(name='rewards_screen'))
            sm.add_widget(AudioMoodTrackerScreen(name='audio_mood_tracker_screen'))
            sm.add_widget(ChatRoomScreen(name='chat_room_screen'))
            sm.add_widget(ReminderScreen(name='reminder_screen'))
            return sm
        except Exception as e:
            logging.error(f"Error setting up the screen manager: {e}")
            return Label(text='An error occurred, please check the logs.')

if __name__ == '__main__':
    MyDailyCompanionApp2().run()
