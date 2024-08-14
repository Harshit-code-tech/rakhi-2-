# home_screen.py
from kivy.uix.screenmanager import Screen


class HomeScreen(Screen):
    def on_pre_enter(self, *args):
        # Check if the auth_screen exists
        auth_screen = self.manager.get_screen('auth_screen')
        if auth_screen:
            self.ids.username_label.text = f"Welcome, {auth_screen.ids.username.text}!"
        else:
            print("Error: auth_screen not found")

    def logout(self):
        self.manager.current = 'auth_screen'
