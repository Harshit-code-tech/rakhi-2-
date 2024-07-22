import logging
import os
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
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

class MoodTrackerScreen(Screen):
    mood_input = ObjectProperty(None)
    moods_list = ObjectProperty(None)

    def submit_mood(self, mood):
        logging.info(f"Mood submitted: {mood}")
        try:
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            file_path = f'data/db/{user_id}/moods.txt'
            moods = read_file(file_path)
            moods.append(mood)
            write_file(file_path, moods)
            self.mood_input.text = ''
            self.load_moods()
        except Exception as e:
            logging.error(f"Error in submit_mood: {e}")

    def delete_mood(self, mood):
        logging.info(f"Deleting mood: {mood}")
        try:
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            file_path = f'data/db/{user_id}/moods.txt'
            moods = read_file(file_path)
            if mood in moods:
                moods.remove(mood)
                write_file(file_path, moods)
                self.load_moods()
        except Exception as e:
            logging.error(f"Error in delete_mood: {e}")

    def on_pre_enter(self):
        self.load_moods()

    def load_moods(self):
        try:
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            file_path = f'data/db/{user_id}/moods.txt'
            moods = read_file(file_path)
            self.display_moods(moods)
        except Exception as e:
            logging.error(f"Error in load_moods: {e}")

    def display_moods(self, moods):
        try:
            self.moods_list.clear_widgets()
            for mood in moods:
                box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                box.add_widget(Label(text=mood, size_hint_x=0.8))
                btn = Button(text='Delete', size_hint_x=0.2)
                btn.bind(on_release=lambda btn, mood=mood: self.delete_mood(mood))
                box.add_widget(btn)
                self.moods_list.add_widget(box)
        except Exception as e:
            logging.error(f"Error in display_moods: {e}")
