from django.urls import path
from django.contrib import admin

from . import views

app_name= 'languages'

urlpatterns = [
    path('search', views.search_by_language, name='search'),
    path('<str:language>/', views.language, name='language'),
]