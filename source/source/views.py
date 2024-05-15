from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
import requests
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

def countries(request):
    data = requests.get("https://restcountries.com/v3.1/lang/spanish").json()
    return render(request, "countries/countries_data.html", {"con":data, "total":len(data)})