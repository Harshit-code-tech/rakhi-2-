from django.contrib import admin
from .models import Mood, Reward, Journal

admin.site.register(Mood)
admin.site.register(Journal)
admin.site.register(Reward)