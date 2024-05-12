from django.urls import path, include
from django.contrib import admin

from . import views

app_name="countries"

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("<str:country>/", views.detail, name="detail"),
]
