from django.urls import path

from . import views

app_name="countries"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:country>/", views.detail, name="detail"),
]