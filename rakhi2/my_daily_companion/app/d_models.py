# d_models.py
import logging
from django.db import models


# Get the logger for this module
logger = logging.getLogger('myapp')

class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        logger.debug(f'Saving MyModel instance: {self}')
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        logger.info(f'Deleting MyModel instance: {self}')
        super().delete(*args, **kwargs)

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
