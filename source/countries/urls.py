

from django.urls import path, include
from django.contrib import admin

from . import views

app_name="countries"

urlpatterns = [
    path('home', views.home, name='home'),
    path('<str:country>/', views.detail, name='detail'),
    path('', views.home, name='home'),
    #path('favoritos/', views.favoritos, name='favoritos'),
    path('currency',views.search_by_currency, name='search_by_currency'),
    path('currency/<str:currency>/', views.currency, name='currency'),
    path('añadir-favorito/', views.añadir_favorito, name='añadir_favorito')
]
