# habit_tracker_screen.py
import logging
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from rakhi2.app.logging_script import read_file, write_file


class HabitTrackerScreen(Screen):
    def submit_habit(self, habit):
        logging.info(f"Habit submitted: {habit}")
        try:
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            write_file(f'data/db/{user_id}/habits.txt', read_file(f'data/db/{user_id}/habits.txt') + [habit])
            self.ids.habit_input.text = ''
            self.load_habits()
        except Exception as e:
            logging.error(f"Error in submit_habit: {e}")

    def delete_habit(self, habit):
        try:
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            habits = read_file(f'data/db/{user_id}/habits.txt')
            if habit in habits:
                habits.remove(habit)
                write_file(f'data/db/{user_id}/habits.txt', habits)
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
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            habits = read_file(f'data/db/{user_id}/habits.txt')
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
