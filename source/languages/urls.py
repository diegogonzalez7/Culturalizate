from django.urls import path
from django.contrib import admin

from . import views

app_name= 'languages'

urlpatterns = [
    path('search', views.search_by_language, name='search_by_language'),
    path('<str:language>/', views.language, name='language'),
]