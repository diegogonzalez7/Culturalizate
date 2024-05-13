from django.urls import path, include
from django.contrib import admin

from . import views

app_name="countries"

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path("<str:country>/", views.detail, name="detail"),
]
