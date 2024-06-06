from django.contrib import admin
from django.urls import include,path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('order', views.order, name='order'),
    path('population_asc/', views.order_by_pop_asc, name='order_by_pop_asc'),
    path('population_desc/', views.order_by_pop_desc, name='order_by_pop_desc'),
    path('area_asc/', views.order_by_area_asc, name='order_by_area_asc'),
    path('area_desc/', views.order_by_area_desc, name='order_by_area_desc')
    ]