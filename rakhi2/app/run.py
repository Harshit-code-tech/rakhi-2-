from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from rakhi2.app.screens.home_screen import HomeScreen
from rakhi2.app.screens.mood_tracker_screen import MoodTrackerScreen
from rakhi2.app.screens.habit_tracker_screen import HabitTrackerScreen
from rakhi2.app.screens.historical_data_screen import HistoricalDataScreen
from rakhi2.app.screens.rewards_screen import RewardsScreen
from rakhi2.app.screens.settings_screen import SettingsScreen
from rakhi2.app.screens.audio_mood_tracker_screen import AudioMoodTrackerScreen
from rakhi2.app.screens.chat_room_screen import ChatRoomScreen
from rakhi2.app.screens.auth_screen import AuthScreen
from rakhi2.app.screens.test_screen import TestScreen
from rakhi2.app.logging_script import setup_logging

setup_logging()

class MyScreenManager(ScreenManager):
    pass

class MyDailyCompanionApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(AuthScreen(name='auth'))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(MoodTrackerScreen(name='mood_tracker'))
        sm.add_widget(HabitTrackerScreen(name='habit_tracker'))
        sm.add_widget(HistoricalDataScreen(name='historical_data'))
        sm.add_widget(RewardsScreen(name='rewards'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(AudioMoodTrackerScreen(name='audio_mood_tracker'))
        sm.add_widget(ChatRoomScreen(name='chat_room'))
        sm.add_widget(TestScreen(name='test'))
        return sm

if __name__ == '__main__':
    MyDailyCompanionApp().run()
