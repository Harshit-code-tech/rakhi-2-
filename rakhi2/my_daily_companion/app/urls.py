from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('signup/', views.signup, name='signup'),
    path('mood_tracker/', views.mood_tracker, name='mood_tracker'),
    path('journal/', views.journal, name='journal'),
    path('set_journal_reminder/', views.set_journal_reminder, name='set_journal_reminder'),
    path('reward/', views.reward, name='reward'),
    path('mood_statistics/', views.mood_statistics, name='mood_statistics'),  # Update to mood_statistics
    path('settings/', views.settings, name='settings'),
    path('reminder/', views.reminder, name='reminder'),
    path('notes/', views.notes, name='notes'),
    path('chatbot_room/', views.chatbot_room, name='chatbot_room'),
    path('delete_reward/<int:reward_id>/', views.delete_reward, name='delete_reward'),
    path('reminder/delete/<int:pk>/', views.delete_reminder, name='delete_reminder'),
    path('delete_note/<int:id>/', views.delete_note, name='delete_note'),
    path('delete_mood/<int:mood_id>/', views.delete_mood, name='delete_mood'),
    path('delete_journal/<int:journal_id>/', views.delete_journal, name='delete_journal'),
    path('delete_reward/<int:reward_id>/', views.delete_reward, name='delete_reward'),
    path('emotion_detection_room/', views.emotion_detection_room, name='emotion_detection_room'),
]
