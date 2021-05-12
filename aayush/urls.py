from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'aayush'
namespace = 'aayush'
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api', include('api.urls', namespace='api')),
              ]