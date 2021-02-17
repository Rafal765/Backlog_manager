from django.views import View
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Genre, GameGenre, Anime, Books, Games, MovieTV, Backlog, BacklogMovieTV, BacklogAnime, BacklogGame, BacklogBook


class GameCardView(View):
    def get(self, request):
        pass
