from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Assuming 'app' is your main app
    path('users/', include('users.urls')),  # Include the URLs for user-related views
]
