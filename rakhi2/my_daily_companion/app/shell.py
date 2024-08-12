import os
import django

# Set the environment variable for Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_daily_companion.settings')

# Setup Django
django.setup()

from app.models import Activity, Mood, Journal, Note, Reward
from django.contrib.auth.models import User

users = User.objects.all()
for user in users:
    activities = Activity.objects.filter(user=user)
    moods = Mood.objects.filter(user=user)
    journals = Journal.objects.filter(user=user)
    notes = Note.objects.filter(user=user)
    rewards = Reward.objects.filter(user=user)

    print(f"Data for {user.username}:")
    print(f"Activities: {activities}")
    print(f"Moods: {moods}")
    print(f"Journals: {journals}")
    print(f"Notes: {notes}")
    print(f"Rewards: {rewards}")
    print("\n")

from app.models import Activity, User

# Print all activities for a specific user
user = User.objects.get(username='testuser2')
activities = Activity.objects.filter(user=user)
print("Activities:", activities)
