# app/urls.py
from rest_framework.routers import DefaultRouter
from .kivy_views import HabitViewSet
from django.urls import path
from django.contrib.auth import views as auth_views
from . import d_views

router = DefaultRouter()
router.register(r'habits', HabitViewSet)

urlpatterns = [
    path('', d_views.home, name='home'),
    path('mood_entries/', d_views.mood_entries, name='mood_entries'),
    path('daily_goals/', d_views.daily_goals, name='daily_goals'),
    # Other URL patterns
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
