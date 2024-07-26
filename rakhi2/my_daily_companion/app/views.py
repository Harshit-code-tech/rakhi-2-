from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Mood, Habit, Reward

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def mood_tracker(request):
    if request.method == 'POST':
        mood = request.POST.get('mood')
        Mood.objects.create(user=request.user, mood=mood)
    return render(request, 'mood_tracker.html')

@login_required
def habit_tracker(request):
    if request.method == 'POST':
        habit = request.POST.get('habit')
        Habit.objects.create(user=request.user, name=habit)
    return render(request, 'habit_tracker.html')

@login_required
def reward(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        Reward.objects.create(user=request.user, image=image)
    return render(request, 'reward.html')

@login_required
def mood_history(request):
    moods = Mood.objects.filter(user=request.user).order_by('-date')
    return render(request, 'mood_history.html', {'moods': moods})

@login_required
def chatbot_room(request):
    return render(request, 'chatbot_room.html')

@login_required
def emotion_detection_room(request):
    return render(request, 'emotion_detection_room.html')

