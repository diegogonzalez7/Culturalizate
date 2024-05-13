from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
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

def detail(request, country):
    return HttpResponse("Information of the countrie %s here." % country)

