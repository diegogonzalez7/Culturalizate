from django.urls import path

from . import views

app_name="countries"

urlpatterns = [
    path('home', views.home, name='home'),
    path('<str:country>/', views.detail, name='detail'),
    path('', views.home, name='home'),
    # Habría que separar favoritos en otra aplicación, dejamos las tres de arriba
    path('add_to_favorites', views.add_to_favorites, name='add_to_favorites'),
    path('show_favorites', views.show_favorites, name='show_favorites')
]
