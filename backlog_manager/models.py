from django.db import models
from django.contrib.auth.models import User


GAME_GENRE_CHOICES = (
    ('ac', "Action"),
    ('aa', "Action-Adventure"),
    ('ad', "Adventure"),
    ('rp', "RPG"),
    ('si', "Simulation"),
    ('st', "Strategy"),
    ('sp', "Sport"),
    ('mm', "MMO"),
    ('vn', "VN"),
)

GENRE_CHOICES = (
    ('ac', "Action"),
    ('co', "Comedy"),
    ('ad', "Adventure"),
    ('cr', "Crime"),
    ('dr', "Drama"),
    ('da', "Fantasy"),
    ('hi', "Historical"),
    ('ho', "Horror"),
    ('sf', "SF"),
    ('th', "Thriller"),
    ('ro', "Romance"),
)


STATUS = (
    ('p', "Planned"),
    ('o', "Ongoing"),
    ('d', "Done"),
)


class GameGenre(models.Model):
    genre = models.CharField(max_length=2, choices=GAME_GENRE_CHOICES)


class Genre(models.Model):
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES)


class Games(models.Model):
    title = models.CharField(max_length=64)
    comment = models.TextField(null=True)
    genre = models.ManyToManyField(GameGenre)


class Anime(models.Model):
    title = models.CharField(max_length=64)
    comment = models.TextField(null=True)
    genre = models.ManyToManyField(Genre)


class MovieTV(models.Model):
    title = models.CharField(max_length=64)
    comment = models.TextField(null=True)
    genre = models.ManyToManyField(Genre)


class Books(models.Model):
    title = models.CharField(max_length=64)
    comment = models.TextField(null=True)
    genre = models.ManyToManyField(Genre)


class Backlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    games = models.ManyToManyField(Games, through=BacklogGame)
    books = models.ManyToManyField(Books, through=BacklogBook)
    anime = models.ManyToManyField(Anime, through=BacklogAnime)
    movies_tv = models.ManyToManyField(MovieTV, through=BacklogMovieTV)


class BacklogGame(models.Model):
    plan = models.ForeignKey(Backlog, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS, default='p')


class BacklogBook(models.Model):
    plan = models.ForeignKey(Backlog, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS, default='p')


class BacklogAnime(models.Model):
    plan = models.ForeignKey(Backlog, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS, default='p')


class BacklogMovieTV(models.Model):
    plan = models.ForeignKey(Backlog, on_delete=models.CASCADE)
    movie_tv = models.ForeignKey(MovieTV, on_delete=models.CASCADE)
    status = models.IntegerField(max_length=1, choices=STATUS, default='p')
