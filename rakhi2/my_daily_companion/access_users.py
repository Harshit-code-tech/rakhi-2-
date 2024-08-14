import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_daily_companion.settings')
django.setup()

from django.contrib.auth.models import User

# Access and print user data
users = User.objects.all()
for user in users:
    print(f'Username: {user.username}, Email: {user.email}, Date Joined: {user.date_joined}')