from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mood_tracker/', views.mood_tracker, name='mood_tracker'),
    path('habit_tracker/', views.habit_tracker, name='habit_tracker'),
    path('reward/', views.reward, name='reward'),
    path('mood_history/', views.mood_history, name='mood_history'),
    path('chatbot_room/', views.chatbot_room, name='chatbot_room'),
    path('emotion_detection_room/', views.emotion_detection_room, name='emotion_detection_room'),
    # Add other URL patterns here

]