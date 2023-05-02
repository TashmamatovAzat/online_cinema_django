from django.views.generic import ListView, DetailView

from .models import Genre, Movie


class GenreListView(ListView):
    model = Genre
    template_name = 'genre.html'
    context_object_name = 'genres'
    fields = "__all__"


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'genre_detail.html'
    context_object_name = 'genre'
    pk_url_kwarg = 'genre_id'


class MovieListView(ListView):
    model = Movie
    template_name = 'movie.html'
    context_object_name = 'movies'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'
    pk_url_kwarg = 'movie_id'
