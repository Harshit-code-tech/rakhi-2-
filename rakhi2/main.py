import logging
from kivy.app import App
from kivy.lang import Builder
from app.views import MyScreenManager

# Configure logging
logging.basicConfig(level=logging.INFO)


class MyDailyCompanionApp(App):
    def build(self):
        logging.info("Loading KV files")
        Builder.load_file('app/templates/home_screen.kv')
        Builder.load_file('app/templates/mood_tracker_screen.kv')
        Builder.load_file('app/templates/habit_tracker_screen.kv')
        Builder.load_file('app/templates/reward_screen.kv')

        logging.info("Building ScreenManager")
        return MyScreenManager()


if __name__ == '__main__':
    logging.info("Starting My Daily Companion App")
    MyDailyCompanionApp().run()
    logging.info("App has stopped")
