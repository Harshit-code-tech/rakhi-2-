from django.urls import path
from app import d_views as views

urlpatterns = [
    path('', views.home, name='home'),
    path('habit_tracker/', views.habit_tracker, name='habit_tracker'),
    path('mood_tracker/', views.mood_tracker, name='mood_tracker'),
    path('historical_data/', views.historical_data, name='historical_data'),
    path('rewards/', views.rewards, name='rewards'),
    path('settings/', views.settings, name='settings'),
    path('reminder/', views.reminder, name='reminder'),
]
