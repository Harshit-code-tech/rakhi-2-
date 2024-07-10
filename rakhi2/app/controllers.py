from app.models import session, User, MoodEntry, DailyGoal
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
