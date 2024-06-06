

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
    path('currency',views.search_by_currency, name='search_by_currency'),
    path('currency/<str:currency>/', views.currency, name='currency'),
    path('añadir-favorito/', views.añadir_favorito, name='añadir_favorito'),
    path('comp_countries/<str:country1>,<str:country2>/', views.comp_countries, name='comp_countries'),
    path('upload', views.upload, name='upload')
]
