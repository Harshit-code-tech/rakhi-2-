import unittest

from rakhi2.app.models import session, MoodEntry, DailyGoal


class TestMyDailyCompanionApp(unittest.TestCase):
    def test_save_mood(self):
        # Example tests for saving mood
        initial_count = session.query(MoodEntry).count()
        new_mood = MoodEntry(user_id=1, mood='happy', date=date.today())
        session.add(new_mood)
        session.commit()
        final_count = session.query(MoodEntry).count()
        self.assertEqual(final_count, initial_count + 1)

    def test_save_goal(self):
        # Example tests for saving goal
        initial_count = session.query(DailyGoal).count()
        new_goal = DailyGoal(user_id=1, goal='exercise', status='incomplete')
        session.add(new_goal)
        session.commit()
        final_count = session.query(DailyGoal).count()
        self.assertEqual(final_count, initial_count + 1)


if __name__ == '__main__':
    unittest.main()
