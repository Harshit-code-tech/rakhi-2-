# chat_room_screen.py
from kivy.uix.screenmanager import Screen

class ChatRoomScreen(Screen):
    def on_pre_enter(self):
        self.ids.chat_log.text = ""

    def send_message(self):
        user_input = self.ids.user_input.text
        response = self.get_gpt2_response(user_input)
        self.ids.chat_log.text += f"User: {user_input}\nBot: {response}\n"
        self.ids.user_input.text = ""

    def get_gpt2_response(self, input_text):
        # Code to get response from Hugging Face GPT-2 model
        pass
