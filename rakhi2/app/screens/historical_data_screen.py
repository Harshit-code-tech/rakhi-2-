import logging

from kivy.uix.screenmanager import Screen

class HistoricalDataScreen(Screen):
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
        except Exception as e:
            logging.error(f"Error in load_data: {e}")

    def display_data(self, moods, habits):
        try:
            self.ids.moods_list.clear_widgets()
            self.ids.habits_list.clear_widgets()
            for mood in moods:
                self.ids.moods_list.add_widget(Label(text=mood))
            for habit in habits:
                self.ids.habits_list.add_widget(Label(text=habit))
        except KeyError as e:
            logging.error(f"KeyError in display_data: {e}")
        except Exception as e:
            logging.error(f"Error in display_data: {e}")