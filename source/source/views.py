from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
import requests
# Create your views here.

def home(request):
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