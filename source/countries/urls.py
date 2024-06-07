from django.urls import path

from . import views

app_name="countries"

urlpatterns = [
    path('home', views.home, name='home'),
    path('<str:country>/', views.detail, name='detail'),
    path('', views.home, name='home'),
    # Habría que separar favoritos en otra aplicación, dejamos las tres de arriba
    path('favoritos/', views.favoritos, name='favoritos'),
    path('añadir-favorito/', views.añadir_favorito, name='añadir_favorito')
]
