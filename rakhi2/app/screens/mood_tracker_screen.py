import logging
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from rakhi2.app.logging_script import read_file, write_file

class MoodTrackerScreen(Screen):
    mood_spinner = ObjectProperty(None)
    custom_mood_input = ObjectProperty(None)
    moods_list = ObjectProperty(None)

    def on_spinner_select(self, spinner, text):
        if text == "Other":
            self.custom_mood_input.disabled = False
            self.custom_mood_input.opacity = 1
        else:
            self.custom_mood_input.disabled = True
            self.custom_mood_input.opacity = 0

    def submit_mood(self):
        mood = self.mood_spinner.text
        if mood == "Other":
            mood = self.custom_mood_input.text
        logging.info(f"Mood submitted: {mood}")
        try:
            user_id = self.manager.get_screen('auth_screen').ids.username.text
            write_file(f'data/db/{user_id}/moods.txt', read_file(f'data/db/{user_id}/moods.txt') + [mood])
            self.mood_spinner.text = 'Select Mood'
            self.custom_mood_input.text = ''
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
            self.moods_list.clear_widgets()
            for mood in moods:
                box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
                box.add_widget(Label(text=mood, size_hint_x=0.8))
                btn = Button(text='Delete', size_hint_x=0.2)
                btn.bind(on_release=lambda btn, mood=mood: self.delete_mood(mood))
                box.add_widget(btn)
                self.moods_list.add_widget(box)
        except KeyError as e:
            logging.error(f"KeyError in display_moods: {e}")
        except Exception as e:
            logging.error(f"Error in display_moods: {e}")
