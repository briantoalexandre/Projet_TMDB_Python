from django.urls import path
from . import views

urlpatterns = [
        path('', views.popular, name='popular'),
        path('popular', views.popular, name='popular'),
        path('topRated', views.topRated, name='topRated'),
        path('genreMovies', views.byGenre, name='genreMovies'),
        path('movieDetail', views.movieDetail, name='movieDetail'),
        path('actorDetail', views.actorDetail, name='actorDetail'),
        path('queryFilms', views.queryFilms, name='queryFilms'),
        path('queryActors', views.queryActors, name='queryActor'),

]