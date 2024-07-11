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
Builder.load_file(os.path.join('app', 'templates', 'rewards_screen.kv'))  # Updated this line

class HomeScreen(Screen):
    pass

class HistoricalDataScreen(Screen):
    def on_pre_enter(self):
        self.load_data()

    def load_data(self):
        moods = self.read_file('moods.txt')
        habits = self.read_file('habits.txt')
        self.display_data(moods, habits)

    def read_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return f.read().splitlines()
        return []

    def display_data(self, moods, habits):
        self.ids.moods_list.clear_widgets()
        self.ids.habits_list.clear_widgets()
        for mood in moods:
            self.ids.moods_list.add_widget(Label(text=mood))
        for habit in habits:
            self.ids.habits_list.add_widget(Label(text=habit))

class MoodTrackerScreen(Screen):
    def submit_mood(self, mood):
        logging.info(f"Mood submitted: {mood}")
        self.save_mood(mood)
        self.ids.mood_input.text = ''
        self.load_moods()

    def save_mood(self, mood):
        with open('moods.txt', 'a') as f:
            f.write(f"{mood}\n")

    def delete_mood(self, mood):
        moods = self.read_file('moods.txt')
        if mood in moods:
            moods.remove(mood)
            self.write_file('moods.txt', moods)
            self.load_moods()

    def read_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return f.read().splitlines()
        return []

    def write_file(self, filename, data):
        with open(filename, 'w') as f:
            for item in data:
                f.write(f"{item}\n")

    def on_pre_enter(self):
        self.load_moods()

    def load_moods(self):
        moods = self.read_file('moods.txt')
        self.display_moods(moods)

    def display_moods(self, moods):
        self.ids.moods_list.clear_widgets()
        for mood in moods:
            box = BoxLayout(orientation='horizontal')
            box.add_widget(Label(text=mood))
            btn = Button(text='Delete', size_hint_x=0.2)
            btn.bind(on_release=lambda btn, mood=mood: self.delete_mood(mood))
            box.add_widget(btn)
            self.ids.moods_list.add_widget(box)

class HabitTrackerScreen(Screen):
    def submit_habit(self, habit):
        logging.info(f"Habit submitted: {habit}")
        self.save_habit(habit)
        self.ids.habit_input.text = ''
        self.load_habits()

    def save_habit(self, habit):
        with open('habits.txt', 'a') as f:
            f.write(f"{habit}\n")

    def delete_habit(self, habit):
        habits = self.read_file('habits.txt')
        if habit in habits:
            habits.remove(habit)
            self.write_file('habits.txt', habits)
            self.load_habits()

    def read_file(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return f.read().splitlines()
        return []

    def write_file(self, filename, data):
        with open(filename, 'w') as f:
            for item in data:
                f.write(f"{item}\n")

    def on_pre_enter(self):
        self.load_habits()

    def load_habits(self):
        habits = self.read_file('habits.txt')
        self.display_habits(habits)

    def display_habits(self, habits):
        self.ids.habits_list.clear_widgets()
        for habit in habits:
            box = BoxLayout(orientation='horizontal')
            box.add_widget(Label(text=habit))
            btn = Button(text='Delete', size_hint_x=0.2)
            btn.bind(on_release=lambda btn, habit=habit: self.delete_habit(habit))
            box.add_widget(btn)
            self.ids.habits_list.add_widget(box)

class RewardsScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        logging.info("Initializing MyScreenManager")
        self.add_widget(HomeScreen(name='home'))
        self.add_widget(MoodTrackerScreen(name='mood_tracker'))
        self.add_widget(HabitTrackerScreen(name='habit_tracker'))
        self.add_widget(RewardsScreen(name='rewards'))
        self.add_widget(HistoricalDataScreen(name='historical_data'))

class MyDailyCompanionApp(App):
    def build(self):
        sm = MyScreenManager()
        return sm

if __name__ == '__main__':
    logging.info("Starting My Daily Companion App")
    MyDailyCompanionApp().run()
