from django.contrib import admin
from django.urls import include,path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('logout', LogoutView.as_view(next_page='/home'), name='logout'),
    path('sign_up', views.sign_up, name='sign_up'),
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