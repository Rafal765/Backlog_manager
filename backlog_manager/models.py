from django.db import models
from django.contrib.auth.models import User


STATUS = (
    ('p', "Planned"),
    ('o', "Ongoing"),
    ('d', "Done"),
)


class GameGenre(models.Model):
    """
    Keep all game specific genres.
    """
    genre = models.CharField(max_length=32)

    def __str__(self):
        return self.genre


class Genre(models.Model):
    """
    Keep all genres.
    """
    genre = models.CharField(max_length=32)

    def __str__(self):
        return self.genre


class Game(models.Model):
    """
    Keep all game instances.
    """
    title = models.CharField(max_length=64)
    comment = models.TextField(null=True)
    genre = models.ManyToManyField(GameGenre)

    def __str__(self):
        return self.title


class Anime(models.Model):
    """
    Keep all anime instances.
    """
    title = models.CharField(max_length=64)
    comment = models.TextField(null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class MovieTV(models.Model):
    """
    Keep all movie and tv series instances.
    """
    title = models.CharField(max_length=64)
    comment = models.TextField(null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Book(models.Model):
    """
    Keep all book instances.
    """
    title = models.CharField(max_length=64)
    comment = models.TextField(null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Backlog(models.Model):
    """
    Keep all user's backlogs.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, default="My backlog")


class BacklogItem(models.Model):
    """
    Main model that keeps all data for specific backlog, each instance relates to one of the game/anime/movie/tv/book,
    each has a status and order number to help organize them.
    """
    plan = models.ForeignKey(Backlog, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, null=True)
    movie_tv = models.ForeignKey(MovieTV, on_delete=models.CASCADE, null=True)
    order = models.PositiveIntegerField()
    status = models.CharField(max_length=1, choices=STATUS, default='p')
