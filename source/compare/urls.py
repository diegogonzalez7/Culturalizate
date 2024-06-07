from django.urls import path, include
from django.contrib import admin

from . import views

app_name= 'compare'

urlpatterns = [
    path('compare_search', views.compare_countries, name='compare_search'),
    path('<str:country1>,<str:country2>/', views.comp_countries, name='comp_countries'),
    path('upload/',include('upload.urls'))
]    