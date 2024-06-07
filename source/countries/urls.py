from django.urls import path

from . import views

app_name="countries"

urlpatterns = [
    path('home', views.home, name='home'),
    path('<str:country>/', views.detail, name='detail'),
    path('', views.home, name='home')
]
