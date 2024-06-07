from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .forms import RegisterForm
from .forms import FavoritoForm
from django.urls import reverse 
from .models import Favorito
import threading
import pandas as pd
import requests, json, time
import matplotlib.pyplot as plt
from requests_oauthlib import OAuth1
import time
from urllib.parse import parse_qs
# pip install googletrans==4.0.0-rc1
from googletrans import Translator

def load_data():
    try:
        with open('all.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []  
    
def load_data_countries(json, country_name):   

    for country in json:
        common_names = [value["common"] for key, value in country["translations"].items()] 
        if country['name']['common'] == country_name:
            return country
        for common_name in common_names:
            if common_name == country_name:
                return country
    return {}

def home(request):
    if request.method == 'POST':
        # Obtener el término de búsqueda del formulario
        country_name = request.POST.get('country_name', None)
        if country_name:
            # Redirigir al usuario a la vista detail del país buscado
            return redirect('countries:detail', country=country_name)
    # Si no hay búsqueda o es una solicitud GET, renderizar la página home
    return render(request, 'countries/home.html')

def detail(request, country):
    start_time = time.time()
    try:
        country_data = None
        weather_data = None

        # Obtener datos del JSON
        countries_data = load_data()  # Supongo que tienes una función llamada load_data()

        country_data = load_data_countries(countries_data, country)

        if not country_data:
            return render(request, 'countries/no_data.html')

        def get_weather_data():
            nonlocal weather_data
            try:
                url2 = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + country + "?key=MCG5889NUL2TSVERVHZGWX4VF"
                response2 = requests.get(url2)
                if response2.status_code == 200:
                    weather_data = response2.json()
                elif response2.status_code == 404:
                    return render(request, 'countries/no_data.html')
                else:
                    return HttpResponse("Error en la solicitud a la segunda API: {}".format(response2.status_code))
            except Exception as e:
                return HttpResponse("Error en la solicitud a la segunda API: {}".format(str(e)))

        thread1 = threading.Thread(target=get_weather_data)
        thread1.start()
        thread1.join()

        if weather_data:
            df_forecast = pd.DataFrame(weather_data.get('days', [])[:7])

            df_forecast['tempmax'] = round((df_forecast['tempmax'] - 32) * 5/9, 1)
            df_forecast['tempmin'] = round((df_forecast['tempmin'] - 32) * 5/9,1)
            df_forecast['temp'] = round((df_forecast['temp'] - 32) * 5/9, 1)

            translator = Translator()
            df_forecast['description'] = df_forecast['description'].apply(lambda x: translator.translate(x, src='en', dest='es').text)

            forecast_data = df_forecast.to_dict(orient='records')

            template = loader.get_template("countries/detail.html")
            context = {
                "country_data": country_data,
                "forecast_data": forecast_data,
            }
            end_time = time.time()
            print(end_time-start_time)
            return HttpResponse(template.render(context, request))
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