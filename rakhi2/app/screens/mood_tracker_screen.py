import logging
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from rakhi2.app.logging_script import read_file, write_file


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