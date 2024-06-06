from django.urls import path
from . import views

app_name = 'capitals'

urlpatterns = [
    path('search', views.search_by_capital, name='search_by_capital'),
    path('<str:capital>/', views.capital, name='capital'),
]
