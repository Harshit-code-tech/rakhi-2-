from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.conf import settings

class Mood(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField()
    MOOD_INTENSITY_CHOICES = [
        ('VL', 'Very Low'),
        ('L', 'Low'),
        ('M', 'Moderate'),
        ('H', 'High'),
        ('VH', 'Very High'),
    ]
    intensity = models.CharField(max_length=2, choices=MOOD_INTENSITY_CHOICES)
    intensity = models.IntegerField(default=0)
    mood = models.CharField(max_length=255)
    custom_mood = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=7, default='#FFFFFF')
    tags = models.CharField(max_length=255, blank=True, null=True)  # Tags or brief description
    sentiment_score = models.FloatField(null=True, blank=True)  # Sentiment score field

    def __str__(self):
        return f"{self.date} - {self.mood}"

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

class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='rewards/', default='img/fallback.png')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reward for {self.user.username} on {self.date}"

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
