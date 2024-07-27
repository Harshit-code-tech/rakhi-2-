from django.contrib import admin
from .models import Mood, Note, Reward

admin.site.register(Mood)
admin.site.register(Note)
admin.site.register(Reward)