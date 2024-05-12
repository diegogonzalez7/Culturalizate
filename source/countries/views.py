from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'countries/home.html')

def detail(request, country):
    return HttpResponse("Information of the countrie %s here." % country)

