# currencies/urls.py
from django.urls import path
from . import views

app_name = "currencies"

urlpatterns = [
    path('search', views.search_by_currency, name='search_by_currency'),
    path('<str:currency>/', views.currency, name='currency'),
]
