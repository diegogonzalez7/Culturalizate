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

def search_by_capital(request):
    if request.method == 'POST':
        # Obtener el término de búsqueda del formulario
        capital_name = request.POST.get('country_capital', None) 
        if capital_name:
            # Redirigir al usuario a la vista capital del país buscado
            return redirect('countries:capital', capital=capital_name)
    # Si no hay búsqueda o es una solicitud GET, renderizar la página b_capital
    return render(request, 'countries/b_capital.html')  

def search_by_currency(request):
    if request.method == 'POST':
        # Obtener el término de búsqueda del formulario
        currency_name = request.POST.get('country_currency', None) 
        if currency_name:
            # Redirigir al usuario a la vista detail del país buscado
            return redirect('countries:currency', currency=currency_name)
    # Si no hay búsqueda o es una solicitud GET, renderizar la página home
    return render(request, 'countries/b_currency.html')  

def capital(request, capital): 
    try:
        url = "https://restcountries.com/v3.1/capital/" + capital
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            template = loader.get_template("countries/capital.html")
            context = {
                "data": data,
            }
            return HttpResponse(template.render(context, request))
        elif response.status_code == 404:
            return render(request, 'countries/no_data.html')
        else:
            return HttpResponse("Error en la solicitud: {}".format(response.status_code))
    except Exception as e:
        return HttpResponse("Error: {}".format(str(e)))




def currency(request, currency): 
    try:    
        url = "https://restcountries.com/v3.1/currency/" + currency
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            template = loader.get_template("countries/currency.html")
            context = {
                "data": data,
            }
            return HttpResponse(template.render(context, request))
        elif response.status_code == 404:
            return render(request, 'countries/no_data.html')
        else:
            return HttpResponse("Error en la solicitud: {}".format(response.status_code))
    except Exception as e:
        return HttpResponse("Error: {}".format(str(e)))

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
    try:
        url = "https://restcountries.com/v3.1/name/" + country
        response = requests.get(url)
        
        # Verificar el código de estado de la respuesta
        if response.status_code == 200:
            data = response.json()
            template = loader.get_template("countries/detail.html")
            context = {
                "data": data,
            }
            return HttpResponse(template.render(context, request))
        elif response.status_code == 404:
            # Si el código de estado es 404, renderizar la plantilla no_data.html
            return render(request, 'countries/no_data.html')
        else:
            # Otro código de estado diferente de 200 o 404, manejar según sea necesario
            return HttpResponse("Error en la solicitud: {}".format(response.status_code))
    except Exception as e:
        # Manejo de otros errores
        return HttpResponse("Error: {}".format(str(e)))

def language(request, language): 
    try:        
        url = "https://restcountries.com/v3.1/lang/" + language
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            template = loader.get_template("countries/language.html")
            context = {
                "data": data,
            }
            return HttpResponse(template.render(context, request))
        elif response.status_code == 404:
            return render(request, 'countries/no_data.html')
        else:
            return HttpResponse("Error en la solicitud: {}".format(response.status_code))
    except Exception as e:
        return HttpResponse("Error: {}".format(str(e)))

def añadir_favorito(request, pais_id):
    if request.method == 'POST':
        pais_nombre = request.POST.get('pais')  # Obtener el nombre del país del formulario POST
        usuario = request.user
        Favorito.objects.create(usuario=usuario, pais=pais_nombre)
        return redirect('favoritos')  # Redirige al usuario a la página de favoritos después de agregar el país

    else:
        form = FavoritoForm()
    return render(request, 'añadir_favorito.html', {'form': form})

def favoritos(request):
    favoritos_usuario = Favorito.objects.filter(usuario=request.user)
    return render(request, 'lista_favoritos.html', {'favoritos_usuario': favoritos_usuario})