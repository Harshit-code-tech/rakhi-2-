from django.contrib import admin
from .models import Mood, Reward, Note, Journal

admin.site.register(Mood)
admin.site.register(Journal)
admin.site.register(Reward)
admin.site.register(Note)
