# d_views.py
from django.shortcuts import render
from django.http import HttpResponse
from .d_models import MoodEntry, DailyGoal


def home(request):
    return HttpResponse("Welcome to My Daily Companion!")
    return render(request, 'home.html')


def mood_entries(request):
    entries = MoodEntry.objects.all()
    return render(request, 'mood_entries.html', {'entries': entries})


def daily_goals(request):
    goals = DailyGoal.objects.all()
    return render(request, 'daily_goals.html', {'goals': goals})
