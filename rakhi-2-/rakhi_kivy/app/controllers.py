# controller.py: This file contains the controller class for the application. It contains methods to save mood and goal data to the database.
from rakhi_kivy.app.kivy_models import session, MoodEntry, DailyGoal
from datetime import date


class AppController:
    def save_mood(self, mood):
        new_mood = MoodEntry(user_id=1, mood=mood, date=date.today())  # Assuming user_id=1 for simplicity
        session.add(new_mood)
        session.commit()

    def save_goal(self, goal):
        new_goal = DailyGoal(user_id=1, goal=goal, status='incomplete')  # Assuming user_id=1 for simplicity
        session.add(new_goal)
        session.commit()
