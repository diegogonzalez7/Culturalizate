from django.urls import include,path
from . import views

urlpatterns = [
    path('', include('countries.urls')),
    path('countries/', include('countries.urls')), # Aplicación de búsqueda por nombre de país
    path('users/', include('users.urls')), # Aplicación de gestión de usuarios
    path('order/', include('order.urls')), # Aplicación de ordenar países por área o población
    path('capitals/', include('capitals.urls')), # Aplicación de búsqueda por capital
    path('languages/', include('languages.urls')), # Aplicación de búsqueda por idioma
    path('upload/', include('upload.urls')), # Aplicación para subir gráficas a Flickr
    path('compare/', include('compare.urls')), # Aplicación de comparación de países
    path('currencies/', include('currencies.urls')), # Aplicación de búsqueda por divisa
    path('favorites/', include('favorites.urls')),
    path("home/", include('countries.urls'))
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
