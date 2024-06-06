from django.urls import path, include
from django.contrib import admin

from . import views

app_name="upload"

urlpatterns = [
    path('', views.upload, name='upload'),
    path('upload', views.upload, name='upload')
]    