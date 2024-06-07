from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
import pandas as pd
import json, time
import time
# Create your views here.

def load_data():
    try:
        with open('all.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def search_by_currency(request):
    if request.method == 'POST':
        # Obtener el término de búsqueda del formulario
        currency_name = request.POST.get('country_currency', None) 
        if currency_name:
            # Redirigir al usuario a la vista detail del país buscado
            return redirect('currencies:currency', currency=currency_name)
    # Si no hay búsqueda o es una solicitud GET, renderizar la página home
    return render(request, 'currencies/b_currency.html')  

def currency(request, currency):
    start_time = time.time() 
    try:    
        countries_data = load_data()
        df = pd.DataFrame(countries_data)

        # Función para verificar si la divisa está presente en el nombre de las divisas
        def has_currency(currencies):
            if isinstance(currencies, dict):
                for value in currencies.values():
                    if currency.capitalize() in value['name']:
                        return True
            return False
        
        # Filtrar los países que tienen la divisa especificada
        df_filtered = df[df['currencies'].apply(has_currency)]
                
        # Ordenar los países
        df_filtered['common_name'] = df_filtered['name'].apply(lambda name: name['common'] if isinstance(name, dict) else None)
        df_sorted = df_filtered.sort_values(by='common_name')

        end_time = time.time()
        print(end_time - start_time)

        template = loader.get_template("currencies/currency.html")
        context = {
            "data": df_sorted.to_dict(orient='records'),
        }
        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return HttpResponse("Error: {}".format(str(e)))