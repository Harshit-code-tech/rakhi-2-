import io

import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend

import base64
import urllib
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from matplotlib import pyplot as plt
from .models import Mood, Note, Reward
from .forms import MoodForm, NoteForm, RewardForm

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
    return render(request, 'mood_tracker.html', {'form': form, 'moods': moods})

@login_required
def notes(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes')
    else:
        form = NoteForm()
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes.html', {'form': form, 'notes': notes})

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
    return render(request, 'reward.html', {'form': form, 'rewards': rewards})

@login_required
def mood_history(request):
    moods = Mood.objects.filter(user=request.user).order_by('date')

    dates = [mood.date for mood in moods]
    mood_levels = [mood.level for mood in moods]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, mood_levels, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Mood Level (0: Very Sad, 5: Neutral, 10: Very Happy)')
    plt.title('Mood History')
    plt.xticks(rotation=45)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)

    return render(request, 'mood_history.html', {'graph': uri})

@login_required
def chatbot_room(request):
    return render(request, 'chatbot_room.html')

@login_required
def emotion_detection_room(request):
    return render(request, 'emotion_detection_room.html')