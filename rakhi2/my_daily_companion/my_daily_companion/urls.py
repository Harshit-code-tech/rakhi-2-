from django.urls import path, include

from app import d_views



urlpatterns = [
    path('app/', include('app.urls')),
    path('auth/', d_views.auth_view, name='auth'),
    path('', d_views.home, name='home'),
    path('habit_tracker/', d_views.habit_tracker, name='habit_tracker'),
    path('mood_tracker/', d_views.mood_tracker, name='mood_tracker'),
    path('historical_data/', d_views.historical_data, name='historical_data'),
    path('rewards/', d_views.rewards, name='rewards'),
    path('settings/', d_views.settings, name='settings'),
    path('reminder/', d_views.reminder, name='reminder'),
]
