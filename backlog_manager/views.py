from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Genre, GameGenre, Anime, Book, Game, MovieTV, Backlog, BacklogItem
from django.forms import ModelForm
#from .forms import BacklogItemGameUpdateForm, BacklogItemAnimeUpdateForm, \
 #   BacklogItemMovieTVUpdateForm, BacklogItemBookUpdateForm
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class MainView(View):
    def get(self, request):
        return render(request, "backlog_manager/main.html")


class BacklogView(View):
    def get(self, request, pk):
        backlog = get_object_or_404(Backlog, pk=pk)
        #backlog_items = BacklogItem.objects.filter(plan=backlog).order_by('order')
        backlog_items_planned = BacklogItem.objects.filter(plan=backlog, status='p').order_by('order')
        backlog_items_ongoing = BacklogItem.objects.filter(plan=backlog, status='o').order_by('order')
        backlog_items_done = BacklogItem.objects.filter(plan=backlog, status='d').order_by('order')
        ctx = {
            "backlog": backlog,
            'backlog_items_planned': backlog_items_planned,
            'backlog_items_ongoing': backlog_items_ongoing,
            'backlog_items_done': backlog_items_done,
        }
        return render(request, "backlog_manager/backlog.html", ctx)


class GameView(View):
    def get(self, request):
        game_list = Game.objects.all().order_by('title')
        ctx = {
            'game_list': game_list,
        }
        return render(request, "backlog_manager/game-list.html", ctx)


class AnimeView(View):
    def get(self, request):
        anime_list = Anime.objects.all().order_by('title')
        ctx = {
            'anime_list': anime_list,
        }
        return render(request, "backlog_manager/anime-list.html", ctx)


class MovieTVView(View):
    def get(self, request):
        movie_tv_list = MovieTV.objects.all().order_by('title')
        ctx = {
            'movie_tv_list': movie_tv_list,
        }
        return render(request, "backlog_manager/movie-tv-list.html", ctx)


class BookView(View):
    def get(self, request):
        book_list = Book.objects.all().order_by('title')
        ctx = {
            'book_list': book_list,
        }
        return render(request, "backlog_manager/book-list.html", ctx)


class GenreView(View):
    def get(self, request):
        genre_list = Genre.objects.all().order_by('genre')
        ctx = {
            'genre_list': genre_list,
        }
        return render(request, "backlog_manager/genre-list.html", ctx)


class GameGenreView(View):
    def get(self, request):
        game_genre_list = GameGenre.objects.all().order_by('genre')
        ctx = {
            'game_genre_list': game_genre_list,
        }
        return render(request, "backlog_manager/game-genre-list.html", ctx)


class GameDetailView(View):
    def get(self, request, pk):
        game = Game.objects.get(pk=pk)
        ctx = {
            'game': game,
        }
        return render(request, "backlog_manager/game-detail.html", ctx)


class AnimeDetailView(View):
    def get(self, request, pk):
        anime = Anime.objects.get(pk=pk)
        ctx = {
            'anime': anime,
        }
        return render(request, "backlog_manager/anime-detail.html", ctx)


class MovieTVDetailView(View):
    def get(self, request, pk):
        movie_tv = MovieTV.objects.get(pk=pk)
        ctx = {
            'movie_tv': movie_tv,
        }
        return render(request, "backlog_manager/movie-tv-detail.html", ctx)


class BookDetailView(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        ctx = {
            'book': book,
        }
        return render(request, "backlog_manager/book-detail.html", ctx)


class GameCreate(CreateView):
    model = Game
    fields = ["title", "comment", "genre"]
    success_url = reverse_lazy("game")


class GameUpdate(UpdateView):
    model = Game
    fields = ["title", "comment", "genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("game")


class GameDelete(DeleteView):
    model = Game
    success_url = reverse_lazy("game")


class AnimeCreate(CreateView):
    model = Anime
    fields = ["title", "comment", "genre"]
    success_url = reverse_lazy("anime")


class AnimeUpdate(UpdateView):
    model = Anime
    fields = ["title", "comment", "genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("anime")


class AnimeDelete(DeleteView):
    model = Anime
    success_url = reverse_lazy("game")


class MovieTVCreate(CreateView):
    model = MovieTV
    fields = ["title", "comment", "genre"]
    success_url = reverse_lazy("movie_tv")


class MovieTVUpdate(UpdateView):
    model = MovieTV
    fields = ["title", "comment", "genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("movie_tv")


class MovieTVDelete(DeleteView):
    model = MovieTV
    success_url = reverse_lazy("movie_tv")


class BookCreate(CreateView):
    model = Book
    fields = ["title", "comment", "genre"]
    success_url = reverse_lazy("book")


class BookUpdate(UpdateView):
    model = Book
    fields = ["title", "comment", "genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("book")


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy("book")


class GameGenreCreate(CreateView):
    model = GameGenre
    fields = ["genre"]
    success_url = reverse_lazy("game_genre")


class GameGenreUpdate(UpdateView):
    model = GameGenre
    fields = ["genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("game_genre")


class GameGenreDelete(DeleteView):
    model = GameGenre
    success_url = reverse_lazy("game_genre")


class GenreCreate(CreateView):
    model = Genre
    fields = ["genre"]
    success_url = reverse_lazy("genre")


class GenreUpdate(UpdateView):
    model = Genre
    fields = ["genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("genre")


class GenreDelete(DeleteView):
    model = Genre
    success_url = reverse_lazy("genre")


class BacklogItemGameAdd(CreateView):
    model = BacklogItem
    fields = ["game", "order", "status"]

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})

    def form_valid(self, form):
        form.instance.plan = Backlog.objects.get(pk=self.kwargs.get('backlog_pk'))
        return super().form_valid(form)


class BacklogItemGameUpdate(UpdateView):
    model = BacklogItem
    fields = ["game", "order", "status"]
    #form_class = BacklogItemGameUpdateForm
    template_name_suffix = "_update_form"

    def form_valid(self, form):
        plan = self.kwargs["backlog_pk"]
        backlog_items = BacklogItem.objects.filter(plan=plan).order_by("order")
        next_order = 1
        for item in backlog_items:
            if next_order == form.cleaned_data["order"]:
                next_order += 1
            item.order = next_order
            next_order += 1
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemGameDelete(DeleteView):
    model = BacklogItem

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


#class BacklogItemAnimeAdd(CreateView):
#    model = BacklogItem
#    fields = ["anime", "order", "status"]
#
#    def get_success_url(self):
#        pk = self.kwargs["backlog_pk"]
#        return reverse_lazy("backlog", kwargs={"pk": pk})
#
#    def form_valid(self, form):
#        form.instance.plan = Backlog.objects.get(pk=self.kwargs.get('backlog_pk'))
#        return super().form_valid(form)
#
#
#class BacklogItemAnimeUpdate(UpdateView):
#    model = BacklogItem
#    #form_class = BacklogItemAnimeUpdateForm
#    template_name_suffix = "_update_form"
#
#    def get_success_url(self):
#        pk = self.kwargs["backlog_pk"]
#        return reverse_lazy("backlog", kwargs={"pk": pk})
#
#
#class BacklogItemAnimeDelete(DeleteView):
#    model = BacklogItem
#
#    def get_success_url(self):
#        pk = self.kwargs["backlog_pk"]
#        return reverse_lazy("backlog", kwargs={"pk": pk})
#
#
#class BacklogItemMovieTVAdd(CreateView):
#    model = BacklogItem
#    fields = ["movie_tv", "order", "status"]
#
#    def get_success_url(self):
#        pk = self.kwargs["backlog_pk"]
#        return reverse_lazy("backlog", kwargs={"pk": pk})
#
#    def form_valid(self, form):
#        form.instance.plan = Backlog.objects.get(pk=self.kwargs.get('backlog_pk'))
#        return super().form_valid(form)
#
#
#class BacklogItemMovieTVUpdate(UpdateView):
#    model = BacklogItem
#    #form_class = BacklogItemMovieTVUpdateForm
#    template_name_suffix = "_update_form"
#
#    def get_success_url(self):
#        pk = self.kwargs["backlog_pk"]
#        return reverse_lazy("backlog", kwargs={"pk": pk})
#
#
#class BacklogItemMovieTVDelete(DeleteView):
#    model = BacklogItem
#
#    def get_success_url(self):
#        pk = self.kwargs["backlog_pk"]
#        return reverse_lazy("backlog", kwargs={"pk": pk})
#
#
#class BacklogItemBookAdd(CreateView):
#    model = BacklogItem
#    fields = ["book", "order", "status"]
#
#    def get_success_url(self):
#        pk = self.kwargs["backlog_pk"]
#        return reverse_lazy("backlog", kwargs={"pk": pk})
#
#    def form_valid(self, form):
#        form.instance.plan = Backlog.objects.get(pk=self.kwargs.get('backlog_pk'))
#        return super().form_valid(form)
#
#
#class BacklogItemBookUpdate(UpdateView):
#    model = BacklogItem
#    #form_class = BacklogItemBookUpdateForm
#    template_name_suffix = "_update_form"
#
#    def get_success_url(self):
#        pk = self.kwargs["backlog_pk"]
#        return reverse_lazy("backlog", kwargs={"pk": pk})
#
#
#class BacklogItemBookDelete(DeleteView):
#    model = BacklogItem
#
#    def get_success_url(self):
#        pk = self.kwargs["backlog_pk"]
#        return reverse_lazy("backlog", kwargs={"pk": pk})


