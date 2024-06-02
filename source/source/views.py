from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import requests, json, time
import pandas as pd
# Create your views here.
# Si queremos requerir el login para el acceso a una vista usaremos @login_required(login_url="/login") antes de ella, redirigiendo a la url si no está logeado

def home(request):
    if request.method == 'POST':
        # Obtener el término de búsqueda del formulario
        country_name = request.POST.get('country_name', None)
        if country_name:
            # Redirigir al usuario a la vista detail del país buscado
            return redirect('countries:detail', country=country_name)
    # Si no hay búsqueda o es una solicitud GET, renderizar la página home
    return render(request, 'countries/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user)
            return redirect('/countries')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form":form})

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
            # Redirigir al usuario a la vista detail del país buscado
            return redirect('countries:capital', capital=capital_name)
    # Si no hay búsqueda o es una solicitud GET, renderizar la página home
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

def countries(request):
    data = requests.get("https://restcountries.com/v3.1/lang/spanish").json()
    return render(request, "countries/countries_data.html", {"con":data, "total":len(data)})

def favoritos(request):
    return redirect('countries:favoritos')

def order(request):
    return render(request, 'countries/order.html')

def load_data():
    try:
        with open('all.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def order_by_pop_asc(request):
    start_time = time.time()
    
    data = load_data()
    if not data:
        return render(request, 'countries/no_data.html', {'message': 'No se pudo cargar la información de los países.'})
    
    data = [country for country in data if 'population' in country]

    try:
        df = pd.DataFrame(data)
    except ValueError as e:
        return render(request, 'countries/no_data.html', {'message': f'Error al convertir datos a DataFrame: {e}'})
    
    df_sorted = df.sort_values(by='population', ascending=True)
    countries_sorted = df_sorted.to_dict(orient='records')

    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    print(f"La vista order_by_pop_asc tardó {tiempo_ejecucion} segundos en ejecutarse.")

    return render(request, 'countries/population.html', {'data': countries_sorted})


def order_by_pop_desc(request):
    start_time = time.time()

    data = load_data()
    if not data:
        return render(request, 'countries/no_data.html', {'message': 'No se pudo cargar la información de los países.'})
    
    data = [country for country in data if 'population' in country]

    try:
        df = pd.DataFrame(data)
    except ValueError as e:
        return render(request, 'countries/no_data.html', {'message': f'Error al convertir datos a DataFrame: {e}'})
    
    df_sorted = df.sort_values(by='population', ascending=False)
    countries_sorted = df_sorted.to_dict(orient='records')

    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    print(f"La vista order_by_pop_desc tardó {tiempo_ejecucion} segundos en ejecutarse.")

    return render(request, 'countries/population.html', {'data': countries_sorted})

def order_by_area_asc(request):
    start_time = time.time()

    data = load_data()
    if not data:
        return render(request, 'countries/no_data.html', {'message': 'No se pudo cargar la información de los países.'})
    
    data = [country for country in data if 'area' in country]

    try:
        df = pd.DataFrame(data)
    except ValueError as e:
        return render(request, 'countries/no_data.html', {'message': f'Error al convertir datos a DataFrame: {e}'})
    
    df_sorted = df.sort_values(by='area', ascending=True)
    countries_sorted = df_sorted.to_dict(orient='records')

    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    print(f"La vista order_by_area_asc tardó {tiempo_ejecucion} segundos en ejecutarse.")

    return render(request, 'countries/area.html', {'data': countries_sorted})

def order_by_area_desc(request):
    start_time = time.time()
    
    data = load_data()
    if not data:
        return render(request, 'countries/no_data.html', {'message': 'No se pudo cargar la información de los países.'})
    
    data = [country for country in data if 'area' in country]

    try:
        df = pd.DataFrame(data)
    except ValueError as e:
        return render(request, 'countries/no_data.html', {'message': f'Error al convertir datos a DataFrame: {e}'})
    
    df_sorted = df.sort_values(by='area', ascending=False)
    countries_sorted = df_sorted.to_dict(orient='records')

    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    print(f"La vista order_by_area_desc tardó {tiempo_ejecucion} segundos en ejecutarse.")

    return render(request, 'countries/area.html', {'data': countries_sorted})