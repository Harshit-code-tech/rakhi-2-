from app.models import Mood
from django.contrib.auth.models import User

# Replace 'your_username' with the username you're testing with
user = User.objects.get(username='testuser2')
moods = Mood.objects.filter(user=user)

print(moods)
