from django.shortcuts import render, redirect
import pandas as pd
import json
import matplotlib.pyplot as plt
from django.template import loader
from django.http import HttpResponse


# Create your views here.

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

def compare_countries(request):
    if request.method == 'POST':
        country1  = request.POST.get('country1', None)
        country2  = request.POST.get('country2', None)
        if country1 and country2:
            return redirect('compare:comp_countries', country1=country1, country2=country2)
    return render(request,'compare/b_comp_countries.html')

def comp_countries(request, country1, country2):

    try: 
        
        data=load_data()

        data_country1=load_data_countries(data,country1)
        data_country2=load_data_countries(data,country2)
        
        template = loader.get_template("compare/comp_countries.html")

        if(data_country1=={} or data_country2=={}):
            return render(request,"countries/no_data.html")


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
    