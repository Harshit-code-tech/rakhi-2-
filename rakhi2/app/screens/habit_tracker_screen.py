import logging
import os
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

# Configure logging
logging.basicConfig(level=logging.INFO)

def read_file(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write('\n'.join(data))

class HabitTrackerScreen(Screen):
    habit_input = ObjectProperty(None)
    habits_list = ObjectProperty(None)

    def submit_habit(self, habit):
        logging.info(f"Habit submitted: {habit}")
        try:
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            file_path = f'data/db/{user_id}/habits.txt'
            habits = read_file(file_path)
            habits.append(habit)
            write_file(file_path, habits)
            self.habit_input.text = ''
            self.load_habits()
        except Exception as e:
            logging.error(f"Error in submit_habit: {e}")

    def delete_habit(self, habit):
        logging.info(f"Deleting habit: {habit}")
        try:
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            file_path = f'data/db/{user_id}/habits.txt'
            habits = read_file(file_path)
            if habit in habits:
                habits.remove(habit)
                write_file(file_path, habits)
                self.load_habits()
        except Exception as e:
            logging.error(f"Error in delete_habit: {e}")

    def on_pre_enter(self):
        self.load_habits()

    def load_habits(self):
        try:
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            file_path = f'data/db/{user_id}/habits.txt'
            habits = read_file(file_path)
            self.display_habits(habits)
        except Exception as e:
            logging.error(f"Error in load_habits: {e}")

    def display_habits(self, habits):
        try:
            self.habits_list.clear_widgets()
            for habit in habits:
                box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                box.add_widget(Label(text=habit, size_hint_x=0.8))
                btn = Button(text='Delete', size_hint_x=0.2)
                btn.bind(on_release=lambda btn, habit=habit: self.delete_habit(habit))
                box.add_widget(btn)
                self.habits_list.add_widget(box)
        except Exception as e:
            logging.error(f"Error in display_habits: {e}")
