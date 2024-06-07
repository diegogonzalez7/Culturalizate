from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
import json

# Create your views here.

def load_data():
    try:
        with open('all.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []  

def add_to_favorites(request):
    if request.method == 'POST':
        country_name = request.POST.get('country_name', None)
        if country_name:
            # Cargar los datos del JSON
            countries_data = load_data()
            # Verificar si el país existe en la lista de países
            country_data = next((country for country in countries_data if country['name']['common'].lower() == country_name.lower()), None)
            if country_data:
                # Obtener la lista de favoritos de la sesión del usuario
                favorites = request.session.get('favorites', [])
                # Verificar si el país ya está en la lista de favoritos
                if country_name not in favorites:
                    favorites.append(country_name)
                    request.session['favorites'] = favorites
                return redirect('favorites:show_favorites')
            else:
                return render(request, 'countries/no_data.html', {'message': 'País no encontrado.'})
    return render(request, 'favorites/add_favorite.html')

def show_favorites(request):
    favorites = request.session.get('favorites', [])
    if not favorites:
        return render(request, 'favorites/no_favorites.html')
    
    # Cargar los datos del JSON
    countries_data = load_data()
    # Filtrar los datos de los países favoritos
    favorite_countries = [country for country in countries_data if country['name']['common'] in favorites]
    
    template = loader.get_template("favorites/show_favorites.html")
    context = {
        "favorite_countries": favorite_countries,
    }
    return HttpResponse(template.render(context, request))