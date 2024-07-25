from django.shortcuts import render
from django.http import HttpResponse
from .models import Mood, Habit, Reward

def home(request):
    return render(request, 'home.html')

def mood_tracker(request):
    if request.method == 'POST':
        mood = request.POST.get('mood')
        Mood.objects.create(user=request.user, mood=mood)
    return render(request, 'mood_tracker.html')

def habit_tracker(request):
    if request.method == 'POST':
        habit = request.POST.get('habit')
        Habit.objects.create(user=request.user, name=habit)
    return render(request, 'habit_tracker.html')

def reward(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        Reward.objects.create(user=request.user, image=image)
    return render(request, 'reward.html')
