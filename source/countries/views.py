from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .forms import RegisterForm
from .forms import FavoritoForm
from django.urls import reverse 
from .models import Favorito
import requests


def home(request):
    if request.method == 'POST':
        # Obtener el término de búsqueda del formulario
        country_name = request.POST.get('country_name', None)
        if country_name:
            # Redirigir al usuario a la vista detail del país buscado
            return redirect('countries:detail', country=country_name)
    # Si no hay búsqueda o es una solicitud GET, renderizar la página home
    return render(request, 'countries/home.html')

def search_by_language(request):
    if request.method == 'POST':
        # Obtener el término de búsqueda del formulario
        language_name = request.POST.get('country_language', None) 
        if language_name:
            # Redirigir al usuario a la vista detail del país buscado
            return redirect('countries:language', language=language_name)
    # Si no hay búsqueda o es una solicitud GET, renderizar la página home
    return render(request, 'countries/b_idioma.html')       

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/home')  # Redirige a la página de inicio después de registrarse
    else:
        form = RegisterForm()
    return render(request, 'countries/sign_up.html', {"form": form})

def detail(request, country):
    data=requests.get("https://restcountries.com/v3.1/name/" + "%s" %country).json()
    template = loader.get_template("countries/detail.html")
    context={
        "data":data,
    }
    return HttpResponse(template.render(context,request))

def language(request, language): 
    data=requests.get("https://restcountries.com/v3.1/lang/" + "%s" %language).json()
    template = loader.get_template("countries/language.html")
    context={
        "data":data,
    }
    return HttpResponse(template.render(context,request))
def añadir_favorito(request, pais_id):
    if request.method == 'POST':
        form = FavoritoForm(request.POST)
        if form.is_valid():
            usuario = request.user
            pais = form.cleaned_data['pais']
            Favorito.objects.create(usuario=usuario, pais=pais)
            return redirect('detalle_pais', pais_id=pais_id)  # Redirigir de vuelta a la página de detalles del país
    else:
        form = FavoritoForm()
    return render(request, 'añadir_favorito.html', {'form': form})

def favoritos(request):
    favoritos_usuario = Favorito.objects.filter(usuario=request.user)
    return render(request, 'favoritos.html', {'favoritos_usuario': favoritos_usuario})