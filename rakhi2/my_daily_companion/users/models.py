from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add other fields as needed
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)