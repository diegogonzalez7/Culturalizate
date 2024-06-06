from django.shortcuts import render
import requests
from requests_oauthlib import OAuth1

# Create your views here.

def upload(request):

    # Claves del consumidor 
    consumer_key = "6bb7d5f2ac85fca1ed7331944d347df2"
    consumer_secret = '081941db6293c397'

    #Claves del cliente
    oauth_token='72157720919853797-aad34a9ab48e0d5e'
    oauth_token_secret='299eddf842906344'

    oauth = OAuth1(client_key=consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=oauth_token,
        resource_owner_secret=oauth_token_secret)
    
    area_photo='countries/static/images/comparison_area.png'
    population_photo='countries/static/images/comparison_population.png'
    density_photo='countries/static/images/comparison_density.png'

    upload_url = 'https://up.flickr.com/services/upload/'
    
    with open(area_photo, 'rb') as photo:
        files = {'photo': photo}
        response = requests.post(upload_url, files=files, auth=oauth)

    with open(population_photo, 'rb') as photo:
        files = {'photo': photo}
        response = requests.post(upload_url, files=files, auth=oauth)

    with open(density_photo, 'rb') as photo:
        files = {'photo': photo}
        response = requests.post(upload_url, files=files, auth=oauth)        

    return render(request, 'upload.html')
