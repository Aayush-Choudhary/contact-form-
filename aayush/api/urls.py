from django.contrib import admin
from django.urls import path,include
from api import views

app_name = 'api'
urlpatterns = [
    path('/message/<str:content>',views.message.as_view(),name='message'),
]