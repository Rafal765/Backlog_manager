"""Projekt_koncowy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from backlog_manager.views import MainView, BacklogView, GameView, AnimeView, MovieTVView, BookView, \
    GameGenreView, GenreView, GameDetailView, AnimeDetailView, MovieTVDetailView, BookDetailView, \
    GameCreate, GameUpdate, GameDelete, AnimeCreate, AnimeUpdate, AnimeDelete, MovieTVCreate, MovieTVUpdate, \
    MovieTVDelete, BookCreate, BookUpdate, BookDelete, GameGenreCreate, GameGenreUpdate, GameGenreDelete, \
    GenreCreate, GenreUpdate, GenreDelete, BacklogItemGameAdd, BacklogItemGameUpdate, BacklogItemGameDelete #, \
   #BacklogItemAnimeAdd, BacklogItemAnimeUpdate, BacklogItemAnimeDelete, BacklogItemMovieTVAdd, BacklogItemMovieTVUpdate, \
   #BacklogItemMovieTVDelete, BacklogItemBookAdd, BacklogItemBookUpdate, BacklogItemBookDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name="homepage"),
    path('backlog/<int:pk>', BacklogView.as_view(), name="backlog"),
    path('game-list/', GameView.as_view(), name="game"),
    path('anime-list/', AnimeView.as_view(), name="anime"),
    path('movie-tv-list/', MovieTVView.as_view(), name="movie_tv"),
    path('book-list/', BookView.as_view(), name="book"),
    path('game-genre-list/', GameGenreView.as_view(), name="game_genre"),
    path('genre-list/', GenreView.as_view(), name="genre"),
    path('game-detail/<int:pk>', GameDetailView.as_view(), name="game_detail"),
    path('anime-detail/<int:pk>', AnimeDetailView.as_view(), name="anime_detail"),
    path('movie-tv-detail/<int:pk>', MovieTVDetailView.as_view(), name="movie_tv_detail"),
    path('book-detail/<int:pk>', BookDetailView.as_view(), name="book_detail"),
    path('game-create/', GameCreate.as_view(), name="game_create"),
    path('game-update/<int:pk>', GameUpdate.as_view(), name="game_update"),
    path('game-delete/<int:pk>', GameDelete.as_view(), name="game_delete"),
    path('anime-create/', AnimeCreate.as_view(), name="anime_create"),
    path('anime-update/<int:pk>', AnimeUpdate.as_view(), name="anime_update"),
    path('anime-delete/<int:pk>', AnimeDelete.as_view(), name="anime_delete"),
    path('movie-tv-create/', MovieTVCreate.as_view(), name="movie_tv_create"),
    path('movie-tv-update/<int:pk>', MovieTVUpdate.as_view(), name="movie_tv_update"),
    path('movie-tv-delete/<int:pk>', MovieTVDelete.as_view(), name="movie_tv_delete"),
    path('book-create/', BookCreate.as_view(), name="book_create"),
    path('book-update/<int:pk>', BookUpdate.as_view(), name="book_update"),
    path('book-delete/<int:pk>', BookDelete.as_view(), name="book_delete"),
    path('game-genre-create/', GameGenreCreate.as_view(), name="game_genre_create"),
    path('game-genre-update/<int:pk>', GameGenreUpdate.as_view(), name="game_genre_update"),
    path('game-genre-delete/<int:pk>', GameGenreDelete.as_view(), name="game_genre_delete"),
    path('genre-create/', GenreCreate.as_view(), name="genre_create"),
    path('genre-update/<int:pk>', GenreUpdate.as_view(), name="genre_update"),
    path('genre-delete/<int:pk>', GenreDelete.as_view(), name="genre_delete"),
    #path('backlog/new-item', BacklogItemAddView.as_view(), name="new_item"),
    path('backlog-item-game-create/<int:backlog_pk>', BacklogItemGameAdd.as_view(), name="backlog_game_create"),
    path('backlog-item-game-update/<int:backlog_pk>/<int:pk>', BacklogItemGameUpdate.as_view(),
         name="backlog_game_update"),
    path('backlog-item-game-delete/<int:backlog_pk>/<int:pk>', BacklogItemGameDelete.as_view(),
         name="backlog_game_delete"),
   # path('backlog-item-anime-create/<int:backlog_pk>', BacklogItemAnimeAdd.as_view(), name="backlog_anime_create"),
   # path('backlog-item-anime-update/<int:backlog_pk>/<int:pk>', BacklogItemAnimeUpdate.as_view(),
   #      name="backlog_anime_update"),
   # path('backlog-item-anime-delete/<int:backlog_pk>/<int:pk>', BacklogItemAnimeDelete.as_view(),
   #      name="backlog_anime_delete"),
   # path('backlog-item-movie-tv-create/<int:backlog_pk>', BacklogItemMovieTVAdd.as_view(),
   #      name="backlog_movie_tv_create"),
   # path('backlog-item-movie-tv-update/<int:backlog_pk>/<int:pk>', BacklogItemMovieTVUpdate.as_view(),
   #      name="backlog_movie_tv_update"),
   # path('backlog-item-movie-tv-delete/<int:backlog_pk>/<int:pk>', BacklogItemMovieTVDelete.as_view(),
   #      name="backlog_movie_tv_delete"),
   # path('backlog-item-book-create/<int:backlog_pk>', BacklogItemBookAdd.as_view(), name="backlog_book_create"),
   # path('backlog-item-book-update/<int:backlog_pk>/<int:pk>', BacklogItemBookUpdate.as_view(),
   #      name="backlog_book_update"),
   # path('backlog-item-book-delete/<int:backlog_pk>/<int:pk>', BacklogItemBookDelete.as_view(),
   #      name="backlog_book_delete"),
]
