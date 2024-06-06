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


def search_by_currency(request):
    if request.method == 'POST':
        # Obtener el término de búsqueda del formulario
        currency_name = request.POST.get('country_currency', None) 
        if currency_name:
            # Redirigir al usuario a la vista detail del país buscado
            return redirect('countries:currency', currency=currency_name)
    # Si no hay búsqueda o es una solicitud GET, renderizar la página home
    return render(request, 'countries/b_currency.html')  

def get_common_name(name_dict):
    return name_dict['common']

def currency(request, currency):
    start_time = time.time() 
    try:    
        url = "https://restcountries.com/v3.1/currency/" + currency
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            #Pasamos a DataFrame con Pandas para ordenarlos
            df = pd.DataFrame(data) 
            df['common_name'] = df['name'].apply(get_common_name)
            #Ordenamos los países según el nombre común
            df_sorted = df.sort_values(by='common_name')

            end_time = time.time()
            print(end_time - start_time)

            template = loader.get_template("countries/currency.html")
            context = {
                "data": df_sorted.to_dict(orient='records'),
            }
            return HttpResponse(template.render(context, request))
        elif response.status_code == 404:
            return render(request, 'countries/no_data.html')
        else:
            return HttpResponse("Error en la solicitud: {}".format(response.status_code))
    except Exception as e:
        return HttpResponse("Error: {}".format(str(e)))


def detail(request, country):
    start_time = time.time()
    try:
        country_data = None
        weather_data = None

        # Obtener datos del JSON
        countries_data = load_data()  # Supongo que tienes una función llamada load_data()

        for country_item in countries_data:
            if country_item['name']['common'].lower() == country.lower():
                country_data = country_item
                break


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


def comp_countries(request, country1, country2):

    try: 
        
        data=load_data()

        data_country1=load_data_countries(data,country1)
        data_country2=load_data_countries(data,country2)
        
        template = loader.get_template("countries/comp_countries.html")


        data = {
            'Country': [country1, country2],
            'Population': [data_country1['population'], data_country2['population']],  # Población en millones
            'Area': [data_country1['area'], data_country2['area']]  # Área en kilómetros cuadrados
        }

        df = pd.DataFrame(data)

        # Calcular la densidad de población
        df['Density'] = df['Population'] / df['Area']

        # Gráfica de comparación de población
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        ax1.bar(df['Country'], df['Population'], color='blue', label='Population')
        ax1.set_xlabel('Country')
        ax1.set_ylabel('Population')
        ax1.set_title('Comparison of Population')
        ax1.legend()

        # Gráfica de comparación de área
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        ax2.bar(df['Country'], df['Area'], color='green', label='Area')
        ax2.set_xlabel('Country')
        ax2.set_ylabel('Area (sq km)')
        ax2.set_title('Comparison of Area')
        ax2.legend()

        # Gráfica de comparación de densidad de población
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        ax3.bar(df['Country'], df['Density'], color='red', label='Density')
        ax3.set_xlabel('Country')
        ax3.set_ylabel('Population Density (people per sq km)')
        ax3.set_title('Comparison of Population Density')
        ax3.legend()

        # Guardar las figuras en archivos
        fig1.savefig('countries/static/images/comparison_population.png')
        fig2.savefig('countries/static/images/comparison_area.png')
        fig3.savefig('countries/static/images/comparison_density.png')

        context = {
            "country1": data_country1,
            "country2": data_country2
        }
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return HttpResponse("Error: {}".format(str(e)))    
    

def upload(request):

    # Claves del consumidor 
    consumer_key = "6bb7d5f2ac85fca1ed7331944d347df2"
    consumer_secret = '081941db6293c397'

    #Claves del cliente
    oauth_token='72157720919853797-aad34a9ab48e0d5e'
    oauth_token_secret='299eddf842906344'

    oauth = OAuth1(client_key=consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=oauth_token,
        resource_owner_secret=oauth_token_secret)

    upload_url = 'https://up.flickr.com/services/upload/'

    with open(photo, 'rb') as photo:
        files = {'photo': photo}
        response = requests.post(upload_url, files=files, auth=oauth)

    return render(request, 'countries/upload.html') 
