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
