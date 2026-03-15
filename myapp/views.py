from django.shortcuts import render
from django.http import HttpResponse
from json import loads
import requests

# Create your views here.

def index(request):
    context = {"movies" : popularMovies()}
    return render(request, 'pages/index.html', context)

# Functions

def popularMovies():
    key = "9e43f45f94705cc8e1d5a0400d19a7b7"
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={key}&language=fr-FR"
    result = requests.get(url)
    return loads(result.text)["results"]
