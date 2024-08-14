# app/views.py
import io
import threading
from datetime import datetime,  timedelta

import matplotlib
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils import timezone
from django.utils.timezone import make_aware
matplotlib.use('Agg')  # Use a non-GUI backend
import plotly.graph_objects as go
import pandas as pd
import base64
import urllib
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from matplotlib import pyplot as plt
from .models import Mood, Reward, Reminder, Note, Journal
from .forms import MoodForm, RewardForm, ReminderForm, NoteForm, JournalForm, JournalReminderForm


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def mood_tracker(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            mood_entry = form.save(commit=False)
            mood_entry.user = request.user  # Set the user field
            mood_entry.save()
            return redirect('mood_tracker')
    else:
        form = MoodForm()
    moods = Mood.objects.filter(user=request.user)  # Filter by user
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
    journals = Journal.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'journal.html', {'form': form, 'journals': journals})

@login_required
def set_journal_reminder(request):
    if request.method == 'POST':
        form = JournalReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            schedule_notification(reminder)  # Schedule the notification
            return redirect('journal')
    else:
        form = JournalReminderForm()
    return render(request, 'set_journal_reminder.html', {'form': form})

def schedule_notification(reminder):
    reminder_time = datetime.combine(reminder.date, reminder.time)
    reminder_time = timezone.make_aware(reminder_time)  # Make reminder_time timezone-aware
    delay = (reminder_time - timezone.now()).total_seconds()
    if delay > 0:
        threading.Timer(delay, send_notification, [reminder]).start()

def send_notification(reminder):
    # Logic to send notification (e.g., using a push notification service)
    print(f"Reminder: {reminder.title} - {reminder.description}")




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
def mood_statistics(request):
    moods = Mood.objects.filter(user=request.user).order_by('date')
    data = pd.DataFrame(list(moods.values('date', 'level', 'mood')), columns=['date', 'level', 'mood'])

    fig = go.Figure()

    for mood_type in data['mood'].unique():
        mood_data = data[data['mood'] == mood_type]
        fig.add_trace(go.Scatter(x=mood_data['date'], y=mood_data['level'], mode='lines+markers', name=mood_type))

    fig.update_layout(title='Mood Statistics',
                      xaxis_title='Date',
                      yaxis_title='Mood Level',
                      legend_title='Mood')

    # Convert Plotly figure to HTML
    graph_html = fig.to_html(full_html=False)

    return render(request, 'mood_statistics.html', {'graph_html': graph_html})

@login_required
def mood_entries(request):
    entries = Mood.objects.filter(user=request.user).order_by('-date')
    return render(request, 'mood_entries.html', {'entries': entries})


@login_required
def delete_mood(request, mood_id):
    mood = get_object_or_404(Mood, id=mood_id, user=request.user)
    mood.delete()
    return redirect('mood_tracker')


@login_required
def reminder(request):
    user_reminders = Reminder.objects.filter(user=request.user)
    if request.method == 'POST':
        form = ReminderForm(request.POST)
        if form.is_valid():
            reminder = form.save(commit=False)
            reminder.user = request.user
            reminder.save()
            schedule_notification(reminder)
            return redirect('reminder')
    else:
        form = ReminderForm()
    return render(request, 'reminder.html', {'reminders': user_reminders, 'form': form})

def schedule_notification(reminder):
    reminder_time = datetime.combine(reminder.date, reminder.time)
    reminder_time = timezone.make_aware(reminder_time)  # Make reminder_time timezone-aware
    delay = (reminder_time - timezone.now()).total_seconds()
    if delay > 0:
        threading.Timer(delay, send_notification, [reminder]).start()

def send_notification(reminder):
    # Logic to send notification (e.g., using a push notification service)
    print(f"Reminder: {reminder.title} - {reminder.description}")


@login_required
def settings(request):
    if request.method == 'POST':
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            return redirect('settings')
    else:
        password_form = PasswordChangeForm(user=request.user)
    return render(request, 'settings.html', {'password_form': password_form})

# @login_required
# def delete_mood(request, mood_id):
#     mood = Mood.objects.get(id=mood_id, user=request.user)
#     mood.delete()
#     return redirect('mood_tracker')

@login_required
def delete_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    return render(request, 'confirm_delete.html', {'object': note})

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

# @login_required
# def delete_reminder(request, reminder_id):
#     reminder = Reminder.objects.get(id=reminder_id, user=request.user)
#     reminder.delete()
#     return redirect('reminder')
@login_required
def delete_reminder(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)
    if request.method == "POST":
        reminder.delete()
        return redirect('reminders')
    return render(request, 'confirm_delete.html', {'object': reminder})

@login_required
def delete_journal(request, journal_id):
    journal = Journal.objects.get(id=journal_id, user=request.user)
    journal.delete()
    return redirect('journal')

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
