from django.urls import path

from . import views


urlpatterns = [
    path('genre/', views.GenreListView.as_view()),
    path('genre/<int:genre_id>', views.GenreDetailView.as_view(), name='genre_detail'),
    path('', views.MovieListView.as_view(), name='list_movie'),
    path('movie/<int:movie_id>', views.MovieDetailView.as_view(), name='movie_detail'),
]