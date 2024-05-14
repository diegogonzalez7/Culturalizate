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
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('admin/', admin.site.urls),
    path("countries/", include("countries.urls")),
    path("sign_up/", include("countries.urls")),
    path("home/", include("countries.urls")),
    path('', include('django.contrib.auth.urls')),
    path('sign_up', views.sign_up, name='sign_up'),
    path('apidata/', views.countries)
]
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
