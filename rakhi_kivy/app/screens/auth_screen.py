# auth_screen.py
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from rakhi_kivy.app.logging_script import authenticate_user, register_user
from kivy.uix.label import Label

class AuthScreen(Screen):
    def __init__(self, **kwargs):
        super(AuthScreen, self).__init__(**kwargs)
        self.authenticated = False

    def login(self):
        user_id = self.ids.username.text
        password = self.ids.password.text

        if authenticate_user(user_id, password):
            self.authenticated = True
            self.manager.current = 'home_screen'
        else:
            popup = Popup(title='Login Failed', content=Label(text='Invalid username or password'), size_hint=(0.6, 0.4))
            popup.open()

    def register(self):
        user_id = self.ids.username.text
        password = self.ids.password.text

        if register_user(user_id, password):
            popup = Popup(title='Registration Successful', content=Label(text='Registration successful! You can now log in.'), size_hint=(0.6, 0.4))
            popup.open()
        else:
            popup = Popup(title='Registration Failed', content=Label(text='User ID already exists'), size_hint=(0.6, 0.4))
            popup.open()
