# d_models.py
from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)

class MoodEntry(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    mood = models.CharField(max_length=100)
    date = models.DateField()

class DailyGoal(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    goal = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
