# app/models.py
from django.contrib.auth.models import User
from django.db import models

class Mood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    level = models.IntegerField()
    mood = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.date} - {self.mood} - {self.level}"

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='rewards/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Reward on {self.date}"

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title