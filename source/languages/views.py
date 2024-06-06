from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
import pandas as pd
import json
import time

def load_data():
    try:
        with open('all.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def search_by_language(request):
    if request.method == 'POST':
        # Obtener el término de búsqueda del formulario
        language_name = request.POST.get('country_language', None)
        if language_name:
            # Redirigir al usuario a la vista detail del país buscado
            return redirect('languages:language', language=language_name)
    # Si no hay búsqueda o es una solicitud GET, renderizar la página home
    return render(request, 'languages/b_idioma.html')  # Ruta actualizada

def language(request, language):
    start_time = time.time()
    try:
        countries_data = load_data()

        df = pd.DataFrame(countries_data)
        
        # Función para verificar si el idioma está en el diccionario de idiomas
        def speaks_language(languages):
            if isinstance(languages, dict):
                return language.capitalize() in languages.values()
            return False
        
        # Filtrar los países que hablan el idioma especificado
        df_filtered = df[df['languages'].apply(speaks_language)]
                
        # Ordenar los países
        df_filtered['common_name'] = df_filtered['name'].apply(lambda name: name['common'] if isinstance(name, dict) else None)
        df_sorted = df_filtered.sort_values(by='common_name')

        context = {
            "data": df_sorted.to_dict(orient='records'),
        }

        end_time = time.time()
        print(end_time - start_time)
        template = loader.get_template("languages/language.html")  # Ruta actualizada

        return HttpResponse(template.render(context, request))
    
    except Exception as e:
        return HttpResponse("Error: {}".format(str(e)))
