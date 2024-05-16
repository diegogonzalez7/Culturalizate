

from django.urls import path, include
from django.contrib import admin

from . import views

app_name="countries"

urlpatterns = [
    path('home', views.home, name='home'),
    path('<str:country>/', views.detail, name='detail'),
    path('', views.home, name='home'),
    path('favoritos/', views.favoritos, name='favoritos'),
    path('language',views.search_by_language, name='search_by_language'),
    path('language/<str:language>/', views.language, name='language'),
]
