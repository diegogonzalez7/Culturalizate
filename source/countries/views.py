from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Aqui iria el buscador para introducir el país")

def detail(request, country):
    return HttpResponse("Information of the countrie %s here." % country)

