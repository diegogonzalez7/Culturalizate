from django.contrib import admin
from django.urls import include,path
from django.contrib.auth.views import LogoutView
from . import views

app_name='order'

urlpatterns = [
    path('order', views.order, name='order'),
    path('population_asc/', views.order_by_pop_asc, name='population_asc'),
    path('population_desc/', views.order_by_pop_desc, name='population_desc'),
    path('area_asc/', views.order_by_area_asc, name='area_asc'),
    path('area_desc/', views.order_by_area_desc, name='area_desc')
    ]