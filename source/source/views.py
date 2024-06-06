from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import login
import requests, json, time
import pandas as pd
from requests_oauthlib import OAuth1
import time
import uuid
from urllib.parse import parse_qs
# Create your views here.

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

def compare_countries(request):
    if request.method == 'POST':
        country1  = request.POST.get('country1', None)
        country2  = request.POST.get('country2', None)
        if country1 and country2:
            return redirect('countries:comp_countries', country1=country1, country2=country2)
    return render(request,'countries/b_comp_countries.html')

def favoritos(request):
    return redirect('countries:favoritos')


def load_data():
    try:
        with open('all.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []


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
    
    area_photo='countries/static/images/comparison_area.png'
    population_photo='countries/static/images/comparison_population.png'
    density_photo='countries/static/images/comparison_density.png'

    upload_url = 'https://up.flickr.com/services/upload/'
    
    with open(area_photo, 'rb') as photo:
        files = {'photo': photo}
        response = requests.post(upload_url, files=files, auth=oauth)

    with open(population_photo, 'rb') as photo:
        files = {'photo': photo}
        response = requests.post(upload_url, files=files, auth=oauth)

    with open(density_photo, 'rb') as photo:
        files = {'photo': photo}
        response = requests.post(upload_url, files=files, auth=oauth)        

    return render(request, 'countries/upload.html')





