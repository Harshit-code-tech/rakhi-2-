from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('app.urls')),
                  path('users/', include('users.urls')),
                  path('login/', user_views.login_view, name='login'),
                  path('logout/', user_views.logout_view, name='logout'),
                  path('register/', user_views.register, name='register'),
              ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
