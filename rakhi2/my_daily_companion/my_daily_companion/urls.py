from django.contrib import admin
from django.urls import path, include
from rakhi2.my_daily_companion.app import d_views  # Import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('', d_views.home, name='home'),  # Add this line for the home view
]
