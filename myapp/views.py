from django.shortcuts import render
from django.http import HttpResponse
from json import loads
import requests

# Pages


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
    context = {"id" : movieIdentifier, "movie" : getMovieDetail(movieIdentifier), "key" : getVideoKey(movieIdentifier), "actors" : getActors(movieIdentifier)}
    return render(request, 'pages/movieDetail.html', context)

def actorDetail(request):
    actorIdentifier = request.GET.get("actorId")
    context = {"id": actorIdentifier, "actor": getActorDetail(actorIdentifier), "movies": getMovies(actorIdentifier)}
    return render(request, 'pages/actorDetail.html', context)

def queryFilms(request):
    query = request.GET.get("query")
    page = request.GET.get("page")
    func = queryGetListMovie(query, page)
    print(func)
    results = func["results"]
    page = func["page"]
    total_pages = func["total_pages"]
    total = func["total_results"]
    context = {"query" : query, "results" : results, "page" : page, "total_pages" : total_pages, "total" : total}

    return render(request, 'pages/queryFilms.html', context)

def queryActors(request):
    query = request.GET.get("query")
    page = request.GET.get("page")
    func = queryGetListActor(query, page)

    results = func["results"]
    page = func["page"]
    total_pages = func["total_pages"]
    total = func["total_results"]
    context = {"query" : query, "results" : results, "page" : page, "total_pages" : total_pages, "total" : total}

    return render(request, 'pages/queryActors.html', context)

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
    check = loads(result.text)["results"]
    if type(check) == list and len(check) != 0:
        check = check[0]
    return check

def getActors(movieId):
    key = "9e43f45f94705cc8e1d5a0400d19a7b7"
    url = f"https://api.themoviedb.org/3/movie/{movieId}/credits?api_key={key}&language=fr-FR"
    result = requests.get(url)
    return loads(result.text)["cast"]

def getActorDetail(actorId):
    key = "9e43f45f94705cc8e1d5a0400d19a7b7"
    url = f"https://api.themoviedb.org/3/person/{actorId}?api_key={key}&language=fr-FR"
    result = requests.get(url)
    return loads(result.text)

def getMovies(actorId):
    key = "9e43f45f94705cc8e1d5a0400d19a7b7"
    url = f"https://api.themoviedb.org/3/person/{actorId}/combined_credits?api_key={key}&language=fr-FR"
    result = requests.get(url)
    return loads(result.text)["cast"]

def queryGetListMovie(query, page):
    if page == None:
        page = 1
    key = "9e43f45f94705cc8e1d5a0400d19a7b7"
    url = f"https://api.themoviedb.org/3/search/movie?query={query}&api_key={key}&language=fr-FR&page={page}"
    result = requests.get(url)
    return loads(result.text)

def queryGetListActor(query, page):
    if page == None:
        page = 1
    key = "9e43f45f94705cc8e1d5a0400d19a7b7"
    url = f"https://api.themoviedb.org/3/search/person?query={query}&api_key={key}&language=fr-FR&page={page}"
    result = requests.get(url)
    return loads(result.text)


t = 943694
print(getVideoKey(t))