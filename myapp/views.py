from django.shortcuts import render
from django.http import HttpResponse
from json import loads
import requests

# Page


def popular(request):
    context = {"movies" : popularMovies()}
    return render(request, 'pages/popular.html', context)

def topRated(request):
    context = {"movies": topRatedMovies()}
    return render(request, 'pages/topRated.html', context)

def byGenre(request):
    identifier = request.GET.get("id")
    context = {"id" : identifier, "movies" : moviesByGenre(identifier)}
    return render(request, 'pages/genreMovies.html', context)

def movieDetail(request):
    movieIdentifier = request.GET.get("movieId")
    context = {"id" : movieIdentifier, "movie" : getMovieDetail(movieIdentifier), "key" : getVideoKey(movieIdentifier)}
    return render(request, 'pages/movieDetail.html', context)

def actorDetail(request):
    pass

# Functions

def popularMovies():
    key = "9e43f45f94705cc8e1d5a0400d19a7b7"
    url = f"https://api.themoviedb.org/3/movie/popular?api_key={key}&language=fr-FR"
    result = requests.get(url)
    return loads(result.text)["results"]

def topRatedMovies():
    key = "9e43f45f94705cc8e1d5a0400d19a7b7"
    url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={key}&language=fr-FR"
    result = requests.get(url)
    return loads(result.text)["results"]

def moviesByGenre(id):
    key = "9e43f45f94705cc8e1d5a0400d19a7b7"
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={key}&language=fr-FR&with_genres={id}"
    result = requests.get(url)
    return loads(result.text)["results"]

def getMovieDetail(movieId):
    key = "9e43f45f94705cc8e1d5a0400d19a7b7"
    url = f"https://api.themoviedb.org/3/movie/{movieId}?api_key={key}&language=fr-FR"
    result = requests.get(url)
    return loads(result.text)

def getVideoKey(movieId):
    key = "9e43f45f94705cc8e1d5a0400d19a7b7"
    url = f"https://api.themoviedb.org/3/movie/{movieId}/videos?api_key={key}&language=fr-FR"
    result = requests.get(url)
    return loads(result.text)
