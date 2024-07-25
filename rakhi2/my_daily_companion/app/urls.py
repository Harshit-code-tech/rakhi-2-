from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mood_tracker/', views.mood_tracker, name='mood_tracker'),
    path('habit_tracker/', views.habit_tracker, name='habit_tracker'),
    path('reward/', views.reward, name='reward'),
]
