# main.py
import logging
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load Kivy files
Builder.load_file(os.path.join('app', 'templates', 'home_screen.kv'))
Builder.load_file(os.path.join('app', 'templates', 'mood_tracker_screen.kv'))
Builder.load_file(os.path.join('app', 'templates', 'habit_tracker_screen.kv'))
Builder.load_file(os.path.join('app', 'templates', 'historical_data_screen.kv'))
Builder.load_file(os.path.join('app', 'templates', 'rewards_screen.kv'))
Builder.load_file(os.path.join('app', 'templates', 'settings_screen.kv'))  # Ensure this line is added


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
            moods = self.read_file('moods.txt')
            habits = self.read_file('habits.txt')
            self.display_data(moods, habits)
        except Exception as e:
            logging.error(f"Error in load_data: {e}")

    def read_file(self, filename):
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    return f.read().splitlines()
            return []
        except Exception as e:
            logging.error(f"Error reading file {filename}: {e}")
            return []

    def display_data(self, moods, habits):
        try:
            if 'moods_list' in self.ids:
                self.ids.moods_list.clear_widgets()
            else:
                logging.error("moods_list ID not found")

            if 'habits_list' in self.ids:
                self.ids.habits_list.clear_widgets()
            else:
                logging.error("habits_list ID not found")

            for mood in moods:
                if 'moods_list' in self.ids:
                    self.ids.moods_list.add_widget(Label(text=mood))
                else:
                    logging.error("moods_list ID not found")

            for habit in habits:
                if 'habits_list' in self.ids:
                    self.ids.habits_list.add_widget(Label(text=habit))
                else:
                    logging.error("habits_list ID not found")
        except KeyError as e:
            logging.error(f"KeyError in display_data: {e}")
        except Exception as e:
            logging.error(f"Error in display_data: {e}")


class MoodTrackerScreen(Screen):
    def submit_mood(self, mood):
        logging.info(f"Mood submitted: {mood}")
        try:
            self.save_mood(mood)
            self.ids.mood_input.text = ''
            self.load_moods()
        except Exception as e:
            logging.error(f"Error in submit_mood: {e}")

    def save_mood(self, mood):
        try:
            with open('moods.txt', 'a') as f:
                f.write(f"{mood}\n")
        except Exception as e:
            logging.error(f"Error saving mood: {e}")

    def delete_mood(self, mood):
        try:
            moods = self.read_file('moods.txt')
            if mood in moods:
                moods.remove(mood)
                self.write_file('moods.txt', moods)
                self.load_moods()
        except Exception as e:
            logging.error(f"Error deleting mood: {e}")

    def read_file(self, filename):
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    return f.read().splitlines()
            return []
        except Exception as e:
            logging.error(f"Error reading file {filename}: {e}")
            return []

    def write_file(self, filename, data):
        try:
            with open(filename, 'w') as f:
                for item in data:
                    f.write(f"{item}\n")
        except Exception as e:
            logging.error(f"Error writing file {filename}: {e}")

    def on_pre_enter(self):
        try:
            self.load_moods()
        except Exception as e:
            logging.error(f"Error in on_pre_enter: {e}")

    def load_moods(self):
        try:
            moods = self.read_file('moods.txt')
            self.display_moods(moods)
        except Exception as e:
            logging.error(f"Error in load_moods: {e}")

    def display_moods(self, moods):
        try:
            if 'moods_list' in self.ids:
                self.ids.moods_list.clear_widgets()
                for mood in moods:
                    box = BoxLayout(orientation='horizontal')
                    box.add_widget(Label(text=mood))
                    btn = Button(text='Delete', size_hint_x=0.2)
                    btn.bind(on_release=lambda btn, mood=mood: self.delete_mood(mood))
                    box.add_widget(btn)
                    self.ids.moods_list.add_widget(box)
            else:
                logging.error("moods_list ID not found")
        except KeyError as e:
            logging.error(f"KeyError in display_moods: {e}")
        except Exception as e:
            logging.error(f"Error in display_moods: {e}")

class HabitTrackerScreen(Screen):
    def submit_habit(self, habit):
        logging.info(f"Habit submitted: {habit}")
        try:
            self.save_habit(habit)
            self.ids.habit_input.text = ''
            self.load_habits()
        except Exception as e:
            logging.error(f"Error in submit_habit: {e}")

    def save_habit(self, habit):
        try:
            with open('habits.txt', 'a') as f:
                f.write(f"{habit}\n")
        except Exception as e:
            logging.error(f"Error saving habit: {e}")

    def delete_habit(self, habit):
        try:
            habits = self.read_file('habits.txt')
            if habit in habits:
                habits.remove(habit)
                self.write_file('habits.txt', habits)
                self.load_habits()
        except Exception as e:
            logging.error(f"Error deleting habit: {e}")

    def read_file(self, filename):
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    return f.read().splitlines()
            return []
        except Exception as e:
            logging.error(f"Error reading file {filename}: {e}")
            return []

    def write_file(self, filename, data):
        try:
            with open(filename, 'w') as f:
                for item in data:
                    f.write(f"{item}\n")
        except Exception as e:
            logging.error(f"Error writing file {filename}: {e}")

    def on_pre_enter(self):
        try:
            self.load_habits()
        except Exception as e:
            logging.error(f"Error in on_pre_enter: {e}")

    def load_habits(self):
        try:
            habits = self.read_file('habits.txt')
            self.display_habits(habits)
        except Exception as e:
            logging.error(f"Error in load_habits: {e}")

    def display_habits(self, habits):
        try:
            if 'habits_list' in self.ids:
                self.ids.habits_list.clear_widgets()
                for habit in habits:
                    box = BoxLayout(orientation='horizontal')
                    box.add_widget(Label(text=habit))
                    btn = Button(text='Delete', size_hint_x=0.2)
                    btn.bind(on_release=lambda btn, habit=habit: self.delete_habit(habit))
                    box.add_widget(btn)
                    self.ids.habits_list.add_widget(box)
            else:
                logging.error("habits_list ID not found")
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

    def read_file(self, filename):
        try:
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    return f.read().splitlines()
            return []
        except Exception as e:
            logging.error(f"Error reading file {filename}: {e}")
            return []

    def display_rewards(self):
        try:
            moods = self.read_file('moods.txt')
            habits = self.read_file('habits.txt')

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
        if mood_count >= 10 and habit_count >= 10:
            return "Congratulations! You've earned a gold star!"
        elif mood_count >= 5 and habit_count >= 5:
            return "Great job! You've earned a silver star!"
        elif mood_count >= 1 and habit_count >= 1:
            return "Good start! You've earned a bronze star!"
        else:
            return "Keep tracking to earn rewards!"


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        logging.info("Initializing MyScreenManager")
        self.add_widget(HomeScreen(name='home'))
        self.add_widget(MoodTrackerScreen(name='mood_tracker'))
        self.add_widget(HabitTrackerScreen(name='habit_tracker'))
        self.add_widget(RewardsScreen(name='rewards'))
        self.add_widget(HistoricalDataScreen(name='historical_data'))
        self.add_widget(SettingsScreen(name='settings'))


class SettingsScreen(Screen):
    pass

class MyDailyCompanionApp(App):
    def build(self):
        sm = MyScreenManager()
        return sm

    def on_kv_post_moods_list(self, instance):
        logging.info(f"moods_list ID set: {instance}")

    def on_kv_post_habits_list(self, instance):
        logging.info(f"habits_list ID set: {instance}")

if __name__ == '__main__':
    logging.info("Starting My Daily Companion App")
    MyDailyCompanionApp().run()

