from django.shortcuts import render
import time, json
import pandas as pd

# Create your views here.

def load_data():
    try:
        with open('all.json', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def order(request):
    return render(request, 'order/order.html')

def order_by_pop_asc(request):
    start_time = time.time()
    
    data = load_data()
    if not data:
        return render(request, 'order/no_data.html', {'message': 'No se pudo cargar la información de los países.'})
    
    data = [country for country in data if 'population' in country]

    try:
        df = pd.DataFrame(data)
    except ValueError as e:
        return render(request, 'order/no_data.html', {'message': f'Error al convertir datos a DataFrame: {e}'})
    
    df_sorted = df.sort_values(by='population', ascending=True)
    countries_sorted = df_sorted.to_dict(orient='records')

    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    print(f"La vista order_by_pop_asc tardó {tiempo_ejecucion} segundos en ejecutarse.")

    return render(request, 'order/population.html', {'data': countries_sorted})


def order_by_pop_desc(request):
    start_time = time.time()

    data = load_data()
    if not data:
        return render(request, 'order/no_data.html', {'message': 'No se pudo cargar la información de los países.'})
    
    data = [country for country in data if 'population' in country]

    try:
        df = pd.DataFrame(data)
    except ValueError as e:
        return render(request, 'order/no_data.html', {'message': f'Error al convertir datos a DataFrame: {e}'})
    
    df_sorted = df.sort_values(by='population', ascending=False)
    countries_sorted = df_sorted.to_dict(orient='records')

    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    print(f"La vista order_by_pop_desc tardó {tiempo_ejecucion} segundos en ejecutarse.")

    return render(request, 'order/population.html', {'data': countries_sorted})

def order_by_area_asc(request):
    start_time = time.time()

    data = load_data()
    if not data:
        return render(request, 'order/no_data.html', {'message': 'No se pudo cargar la información de los países.'})
    
    data = [country for country in data if 'area' in country]

    try:
        df = pd.DataFrame(data)
    except ValueError as e:
        return render(request, 'order/no_data.html', {'message': f'Error al convertir datos a DataFrame: {e}'})
    
    df_sorted = df.sort_values(by='area', ascending=True)
    countries_sorted = df_sorted.to_dict(orient='records')

    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    print(f"La vista order_by_area_asc tardó {tiempo_ejecucion} segundos en ejecutarse.")

    return render(request, 'order/area.html', {'data': countries_sorted})

def order_by_area_desc(request):
    start_time = time.time()
    
    data = load_data()
    if not data:
        return render(request, 'order/no_data.html', {'message': 'No se pudo cargar la información de los países.'})
    
    data = [country for country in data if 'area' in country]

    try:
        df = pd.DataFrame(data)
    except ValueError as e:
        return render(request, 'order/no_data.html', {'message': f'Error al convertir datos a DataFrame: {e}'})
    
    df_sorted = df.sort_values(by='area', ascending=False)
    countries_sorted = df_sorted.to_dict(orient='records')

    end_time = time.time()
    tiempo_ejecucion = end_time - start_time
    print(f"La vista order_by_area_desc tardó {tiempo_ejecucion} segundos en ejecutarse.")

    return render(request, 'order/area.html', {'data': countries_sorted})