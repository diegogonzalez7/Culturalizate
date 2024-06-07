from django.urls import path
from . import views

app_name = "favorites"

urlpatterns = [
    path('add_to_favorites', views.add_to_favorites, name='add_to_favorites'),
    path('show_favorites', views.show_favorites, name='show_favorites')
]
