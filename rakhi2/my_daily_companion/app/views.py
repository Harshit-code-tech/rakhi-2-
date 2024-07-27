from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mood, Habit, Reward
from .forms import MoodForm, HabitForm, RewardForm

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def mood_tracker(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            mood = form.save(commit=False)
            mood.user = request.user
            mood.save()
            return redirect('mood_tracker')
    else:
        form = MoodForm()
    moods = Mood.objects.filter(user=request.user)
    return render(request, 'app/mood_tracker.html', {'form': form, 'moods': moods})

@login_required
def habit_tracker(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('habit_tracker')
    else:
        form = HabitForm()
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'app/habit_tracker.html', {'form': form, 'habits': habits})

@login_required
def reward(request):
    if request.method == 'POST':
        form = RewardForm(request.POST, request.FILES)
        if form.is_valid():
            reward = form.save(commit=False)
            reward.user = request.user
            reward.save()
            return redirect('reward')
    else:
        form = RewardForm()
    rewards = Reward.objects.filter(user=request.user)
    return render(request, 'app/reward.html', {'form': form, 'rewards': rewards})

@login_required
def mood_history(request):
    moods = Mood.objects.filter(user=request.user)
    return render(request, 'app/mood_history.html', {'moods': moods})

@login_required
def chatbot_room(request):
    return render(request, 'app/chatbot_room.html')

@login_required
def emotion_detection_room(request):
    return render(request, 'app/emotion_detection_room.html')
