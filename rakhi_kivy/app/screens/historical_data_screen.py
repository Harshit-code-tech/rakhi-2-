# historical_data_screen.py
import logging
import os
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
import matplotlib.pyplot as plt
from kivy.uix.image import Image as KivyImage

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

class HistoricalDataScreen(Screen):
    moods_list = ObjectProperty(None)
    habits_list = ObjectProperty(None)

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
            self.plot_data(moods, habits, user_id)
        except Exception as e:
            logging.error(f"Error in load_data: {e}")

    def display_data(self, moods, habits):
        try:
            self.moods_list.clear_widgets()
            self.habits_list.clear_widgets()
            for mood in moods:
                self.moods_list.add_widget(Label(text=mood))
            for habit in habits:
                self.habits_list.add_widget(Label(text=habit))
        except KeyError as e:
            logging.error(f"KeyError in display_data: {e}")
        except Exception as e:
            logging.error(f"Error in display_data: {e}")

    def plot_data(self, moods, habits, user_id):
        try:
            # Generate a plot for mood and habit data over time
            plt.figure(figsize=(10, 5))
            plt.plot(moods, label='Moods')
            plt.plot(habits, label='Habits')
            plt.xlabel('Time')
            plt.ylabel('Entries')
            plt.title('Mood and Habit Tracker')
            plt.legend()
            plot_path = f'data/db/{user_id}/plot.png'
            plt.savefig(plot_path)
            plt.close()

            # Display the plot in the Kivy interface
            if os.path.exists(plot_path):
                self.ids.plot_image.source = plot_path
        except Exception as e:
            logging.error(f"Error in plot_data: {e}")
