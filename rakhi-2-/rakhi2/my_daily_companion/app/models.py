# app/models.py
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings


class Mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    mood = models.CharField(max_length=255)
    intensity = models.FloatField()
    color = models.CharField(max_length=7)
    tags = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.mood}"


class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class JournalReminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='Journal Reminder')
    description = models.TextField(default='Time to write in your journal!')
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_url = models.URLField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=20, default='locked')  # Status can be 'locked' or 'unlocked'
    date_unlocked = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.user.username}'


class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='rewards/')
    is_unlocked = models.BooleanField(default=False)
    date_unlocked = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Reward for {self.user.username}'


# Example Activity model
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    count = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)  # or auto_now=True if it should update on save

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.date}"


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
