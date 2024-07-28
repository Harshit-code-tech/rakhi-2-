# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mood_tracker/', views.mood_tracker, name='mood_tracker'),
    #path('notes/', views.notes, name='notes'),  # Updated from habit_tracker to notes
    path('journal/', views.journal, name='journal'),
    path('reward/', views.reward, name='reward'),
    path('mood_history/', views.mood_history, name='mood_history'),
    path('settings/', views.settings, name='settings'),
    path('reminder/', views.reminder, name='reminder'),
    path('chatbot_room/', views.chatbot_room, name='chatbot_room'),
    path('delete_reward/<int:reward_id>/', views.delete_reward, name='delete_reward'),
    path('delete_reminder/<int:reminder_id>/', views.delete_reminder, name='delete_reminder'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('delete_mood/<int:mood_id>/', views.delete_mood, name='delete_mood'),
    path('emotion_detection_room/', views.emotion_detection_room, name='emotion_detection_room'),
]
