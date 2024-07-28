# app/views.py
import io
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import plotly.graph_objects as go
import pandas as pd
import base64
import urllib
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from matplotlib import pyplot as plt
from .models import Mood, Reward, Reminder, Journal
from .forms import MoodForm, JournalForm, RewardForm, ReminderForm

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
def journal(request):
    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.user = request.user
            journal.save()
            return redirect('journal')
    else:
        form = JournalForm()
    journals = Journal.objects.filter(user=request.user)
    return render(request, 'journal.html', {'form': form, 'journals': journals})

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
    data = pd.DataFrame(list(moods.values('date', 'level', 'mood')), columns=['date', 'level', 'mood'])

    fig = go.Figure()

    for mood_type in data['mood'].unique():
        mood_data = data[data['mood'] == mood_type]
        fig.add_trace(go.Scatter(x=mood_data['date'], y=mood_data['level'], mode='lines+markers', name=mood_type))

    fig.update_layout(title='Mood History',
                      xaxis_title='Date',
                      yaxis_title='Mood Level',
                      legend_title='Mood Type',
                      xaxis=dict(tickformat='%Y-%m-%d'))

    graph_html = fig.to_html(full_html=False)
    return render(request, 'mood_history.html', {'graph': graph_html})

@login_required
def reminder(request):
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            return redirect('reminder')
    else:
        form = ReminderForm()
    reminders = Reminder.objects.filter(user=request.user)
    return render(request, 'reminder.html', {'form': form, 'reminders': reminders})

@login_required
def settings(request):
    return render(request, 'settings.html')

@login_required
def delete_mood(request, mood_id):
    mood = Mood.objects.get(id=mood_id, user=request.user)
    mood.delete()
    return redirect('mood_tracker')

@login_required
def delete_note(request, note_id):
    note = Note.objects.get(id=note_id, user=request.user)
    note.delete()
    return redirect('notes')

@login_required
def chatbot_room(request):
    return render(request, 'chatbot_room.html')

@login_required
def emotion_detection_room(request):
    return render(request, 'emotion_detection_room.html')

@login_required
def delete_reward(request, reward_id):
    reward = Reward.objects.get(id=reward_id, user=request.user)
    reward.delete()
    return redirect('reward')

@login_required
def delete_reminder(request, reminder_id):
    reminder = Reminder.objects.get(id=reminder_id, user=request.user)
    reminder.delete()
    return redirect('reminder')
