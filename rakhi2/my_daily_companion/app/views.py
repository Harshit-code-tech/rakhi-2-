from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mood, Habit, Reward

def home(request):
    return render(request, 'home.html')

@login_required
def mood_tracker(request):
    if request.method == 'POST':
        mood = request.POST.get('mood')
        if mood:
            Mood.objects.create(user=request.user, mood=mood)
            return redirect('mood_tracker')
    moods = Mood.objects.filter(user=request.user)
    return render(request, 'mood_tracker.html', {'moods': moods})

@login_required
def habit_tracker(request):
    if request.method == 'POST':
        habit = request.POST.get('habit')
        if habit:
            Habit.objects.create(user=request.user, name=habit)
            return redirect('habit_tracker')
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'habit_tracker.html', {'habits': habits})

@login_required
def reward(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        if image:
            Reward.objects.create(user=request.user, image=image)
            return redirect('reward')
    rewards = Reward.objects.filter(user=request.user)
    return render(request, 'reward.html', {'rewards': rewards})
