"""
URL configuration for source project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('countries/', include('countries.urls')),
    path("home/", include('countries.urls')),
    path('', include('django.contrib.auth.urls')),
    path('logout', LogoutView.as_view(next_page='/home'), name='logout'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('apidata/', views.countries),
    path('language',views.search_by_language, name='search_by_language'),
    path('capital',views.search_by_capital, name='search_by_capital'),
    path('currency',views.search_by_currency, name='search_by_currency'),
    path('favoritos',views.favoritos, name='favoritos'),
    path('order', views.order, name='order'),
    path('population_asc/', views.order_by_pop_asc, name='order_by_pop_asc'),
    path('population_desc/', views.order_by_pop_desc, name='order_by_pop_desc'),
    path('area_asc/', views.order_by_area_asc, name='order_by_area_asc'),
    path('area_desc/', views.order_by_area_desc, name='order_by_area_desc'),
    path('comp_countries', views.compare_countries, name='compare')]
"""
django.contrib.auth.urls incluye los siguientes patrones URL:
    /login/ [name='login']
    /logout/ [name='logout']
    /password_change/ [name='password_change']
    /password_change/done/ [name='password_change_done']
    /password_reset/ [name='password_reset']
    /password_reset/done/ [name='password_reset_done']
    /reset/<uidb64>/<token>/ [name='password_reset_confirm']
    /reset/done/ [name='password_reset_complete']
"""
