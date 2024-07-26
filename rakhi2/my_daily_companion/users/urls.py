from django.urls import path
from .views import register, login_view
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    # Add other paths if needed
]
