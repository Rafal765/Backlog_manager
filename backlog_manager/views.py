from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Genre, GameGenre, Anime, Book, Game, MovieTV, Backlog, BacklogItem
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class MainView(LoginRequiredMixin, View):
    """
    Display a list of logged user's backlogs and links to manage entries.
    Template: `backlog_manager/my-backlogs.html`
    """
    login_url = "login"

    def get(self, request):
        return render(request, "backlog_manager/my-backlogs.html")


class BacklogCreate(LoginRequiredMixin, CreateView):
    """
    Display a form to add a new backlog for logged user.
    Template: `backlog_manager/backlog_form.html`
    """
    login_url = "login"

    model = Backlog
    fields = ["name"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("my_backlogs")


class BacklogUpdate(LoginRequiredMixin, UpdateView):
    """
    Display a form to update a name for backlog.
    Template: `backlog_manager/backlog_update_form.html`
    """
    login_url = "login"

    model = Backlog
    fields = ["name"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("my_backlogs")


class BacklogDelete(LoginRequiredMixin, DeleteView):
    """
    Display a confirmation to delete a backlog entry in the database.
    Template:`backlog_manager/backlog_confirm_delete.html`
    """
    login_url = "login"

    model = Backlog

    def get_success_url(self):
        return reverse_lazy("my_backlogs")


class BacklogView(LoginRequiredMixin, View):
    """
    Display a list of all entries in a backlog, organized by their status.
    Template: `backlog_manager/backlog.html`
    """
    login_url = "login"

    def get(self, request, pk):
        backlog = get_object_or_404(Backlog, pk=pk)
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


class GameView(LoginRequiredMixin, View):
    """
    Display a list of all games in the database.
    Template: `backlog_manager/game-list.html`
    """
    login_url = "login"

    def get(self, request):
        game_list = Game.objects.all().order_by('title')
        ctx = {
            'game_list': game_list,
        }
        return render(request, "backlog_manager/game-list.html", ctx)


class AnimeView(LoginRequiredMixin, View):
    """
    Display a list of all anime in the database.
    Template: `backlog_manager/anime-list.html`
    """
    login_url = "login"

    def get(self, request):
        anime_list = Anime.objects.all().order_by('title')
        ctx = {
            'anime_list': anime_list,
        }
        return render(request, "backlog_manager/anime-list.html", ctx)


class MovieTVView(LoginRequiredMixin, View):
    """
    Display a list of all movie and TV series in the database.
    Template: `backlog_manager/movie-tv-list.html`
    """
    login_url = "login"

    def get(self, request):
        movie_tv_list = MovieTV.objects.all().order_by('title')
        ctx = {
            'movie_tv_list': movie_tv_list,
        }
        return render(request, "backlog_manager/movie-tv-list.html", ctx)


class BookView(LoginRequiredMixin, View):
    """
    Display a list of all books in the database.
    Template: `backlog_manager/book-list.html`
    """
    login_url = "login"

    def get(self, request):
        book_list = Book.objects.all().order_by('title')
        ctx = {
            'book_list': book_list,
        }
        return render(request, "backlog_manager/book-list.html", ctx)


class GenreView(LoginRequiredMixin, View):
    """
    Display a list of all standard genres in the database.
    Template:`backlog_manager/genre-list.html`
    """
    login_url = "login"

    def get(self, request):
        genre_list = Genre.objects.all().order_by('genre')
        ctx = {
            'genre_list': genre_list,
        }
        return render(request, "backlog_manager/genre-list.html", ctx)


class GameGenreView(LoginRequiredMixin, View):
    """
    Display a list of all game specific genres in the database.
    Template: `backlog_manager/game-genre-list.html`
    """
    login_url = "login"

    def get(self, request):
        game_genre_list = GameGenre.objects.all().order_by('genre')
        ctx = {
            'game_genre_list': game_genre_list,
        }
        return render(request, "backlog_manager/game-genre-list.html", ctx)


class GameDetailView(LoginRequiredMixin, View):
    """
    Display detail page for game instance.
    Template: `backlog_manager/game-detail.html`
    """
    login_url = "login"

    def get(self, request, pk):
        game = Game.objects.get(pk=pk)
        ctx = {
            'game': game,
        }
        return render(request, "backlog_manager/game-detail.html", ctx)


class AnimeDetailView(LoginRequiredMixin, View):
    """
    Display detail page for anime instance.
    Template: `backlog_manager/anime-detail.html`
    """
    login_url = "login"

    def get(self, request, pk):
        anime = Anime.objects.get(pk=pk)
        ctx = {
            'anime': anime,
        }
        return render(request, "backlog_manager/anime-detail.html", ctx)


class MovieTVDetailView(LoginRequiredMixin, View):
    """
    Display detail page for movie/tv instance.
    Template: `backlog_manager/movie-tv-detail.html`
    """
    login_url = "login"

    def get(self, request, pk):
        movie_tv = MovieTV.objects.get(pk=pk)
        ctx = {
            'movie_tv': movie_tv,
        }
        return render(request, "backlog_manager/movie-tv-detail.html", ctx)


class BookDetailView(LoginRequiredMixin, View):
    """
    Display detail page for book instance.
    Template: `backlog_manager/book-detail.html`
    """
    login_url = "login"

    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        ctx = {
            'book': book,
        }
        return render(request, "backlog_manager/book-detail.html", ctx)


class GameCreate(LoginRequiredMixin, CreateView):
    """
    Display a form to add a new game.
    Template: `backlog_manager/game_form.html`
    """
    login_url = "login"

    model = Game
    fields = ["title", "comment", "genre"]
    success_url = reverse_lazy("game")


class GameUpdate(LoginRequiredMixin, UpdateView):
    """
    Display a form to update a game entry in the database.
    Template: `backlog_manager/game_update_form.html`
    """
    login_url = "login"

    model = Game
    fields = ["title", "comment", "genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("game")


class GameDelete(LoginRequiredMixin, DeleteView):
    """
    Display a confirmation to delete a game entry in the database.
    Template:`backlog_manager/game_confirm_delete.html`
    """
    login_url = "login"

    model = Game
    success_url = reverse_lazy("game")


class AnimeCreate(LoginRequiredMixin, CreateView):
    """
    Display a form to add a new anime.
    Template: `backlog_manager/anime_form.html`
    """
    login_url = "login"

    model = Anime
    fields = ["title", "comment", "genre"]
    success_url = reverse_lazy("anime")


class AnimeUpdate(LoginRequiredMixin, UpdateView):
    """
    Display a form to update an anime entry in the database.
    Template: `backlog_manager/anime_update_form.html`
    """
    login_url = "login"

    model = Anime
    fields = ["title", "comment", "genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("anime")


class AnimeDelete(LoginRequiredMixin, DeleteView):
    """
    Display a confirmation to delete an anime entry in the database.
    Template:`backlog_manager/anime_confirm_delete.html`
    """
    login_url = "login"

    model = Anime
    success_url = reverse_lazy("game")


class MovieTVCreate(LoginRequiredMixin, CreateView):
    """
    Display a form to add a new movie/tv.
    Template:`backlog_manager/movietv_form.html`
    """
    login_url = "login"

    model = MovieTV
    fields = ["title", "comment", "genre"]
    success_url = reverse_lazy("movie_tv")


class MovieTVUpdate(LoginRequiredMixin, UpdateView):
    """
    Display a form to update a movie or tv series entry in the database.
    Template: `backlog_manager/movietv_update_form.html`
    """
    login_url = "login"

    model = MovieTV
    fields = ["title", "comment", "genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("movie_tv")


class MovieTVDelete(LoginRequiredMixin, DeleteView):
    """
    Display a confirmation to delete a movie or tv series entry in the database.
    Template:`backlog_manager/movietv_confirm_delete.html`
    """
    login_url = "login"

    model = MovieTV
    success_url = reverse_lazy("movie_tv")


class BookCreate(LoginRequiredMixin, CreateView):
    """
    Display a form to add a new book.
    Template:`backlog_manager/game_form.html`
    """
    login_url = "login"

    model = Book
    fields = ["title", "comment", "genre"]
    success_url = reverse_lazy("book")


class BookUpdate(LoginRequiredMixin, UpdateView):
    """
    Display a form to update a book entry in the database.
    Template: `backlog_manager/book_update_form.html`
    """
    login_url = "login"

    model = Book
    fields = ["title", "comment", "genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("book")


class BookDelete(LoginRequiredMixin, DeleteView):
    """
    Display a confirmation to delete a book entry in the database.
    Template:`backlog_manager/book_confirm_delete.html`
    """
    login_url = "login"

    model = Book
    success_url = reverse_lazy("book")


class GameGenreCreate(LoginRequiredMixin, CreateView):
    """
    Display a form to add a new game genre.
    Template:`backlog_manager/gamegenre_form.html`
    """
    login_url = "login"

    model = GameGenre
    fields = ["genre"]
    success_url = reverse_lazy("game_genre")


class GameGenreUpdate(LoginRequiredMixin, UpdateView):
    """
    Display a form to update a game genre entry in the database.
    Template: `backlog_manager/gamegenre_update_form.html`
    """
    login_url = "login"

    model = GameGenre
    fields = ["genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("game_genre")


class GameGenreDelete(LoginRequiredMixin, DeleteView):
    """
    Display a confirmation to delete a game genre entry in the database.
    Template:`backlog_manager/gamegenre_confirm_delete.html`
    """
    login_url = "login"

    model = GameGenre
    success_url = reverse_lazy("game_genre")


class GenreCreate(LoginRequiredMixin, CreateView):
    """
    Display a form to add a new genre.
    Template:`backlog_manager/genre_form.html`
    """
    login_url = "login"

    model = Genre
    fields = ["genre"]
    success_url = reverse_lazy("genre")


class GenreUpdate(LoginRequiredMixin, UpdateView):
    """
    Display a form to update a genre entry in the database.
    Template: `backlog_manager/genre_update_form.html`
    """
    login_url = "login"

    model = Genre
    fields = ["genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("genre")


class GenreDelete(LoginRequiredMixin, DeleteView):
    """
    Display a confirmation to delete a genre entry in the database.
    Template:`backlog_manager/genre_confirm_delete.html`
    """
    login_url = "login"

    model = Genre
    success_url = reverse_lazy("genre")


class BacklogItemGameAdd(LoginRequiredMixin, CreateView):
    """
    Display a form to add an item to backlog, from existing games.
    Template:`backlog_manager/backlogitem_form.html`
    """
    login_url = "login"

    model = BacklogItem
    fields = ["game", "status"]

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})

    def form_valid(self, form):
        # Save plan id to database
        form.instance.plan = Backlog.objects.get(pk=self.kwargs.get('backlog_pk'))
        # Gives next available order
        plan = self.kwargs["backlog_pk"]
        status = form.instance.status
        backlog_items = BacklogItem.objects.filter(plan=plan).filter(status=status).order_by("order")
        next_order = 1
        for item in backlog_items:
            next_order += 1
        form.instance.order = next_order
        return super().form_valid(form)


class BacklogItemGameUpdate(LoginRequiredMixin, UpdateView):
    """
    Display a form to update a game entry in the backlog.
    Template:`backlog_manager/backlogitem_update_form.html`
    """
    login_url = "login"

    model = BacklogItem
    fields = ["game", "order", "status"]
    template_name_suffix = "_update_form"

    def form_valid(self, form):
        plan = self.kwargs["backlog_pk"]
        status = form.instance.status
        backlog_items = list(BacklogItem.objects.filter(plan=plan).filter(status=status).order_by("order"))
        next_order = 1
        for item in backlog_items:
            if next_order == form.cleaned_data["order"]:
                next_order += 1
            item.order = next_order
            next_order += 1
        BacklogItem.objects.bulk_update(backlog_items, ["order"])
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemGameDelete(LoginRequiredMixin, DeleteView):
    """
    Display a confirmation to delete a game entry in the backlog.
    Template:`backlog_manager/backlogitem_confirm_delete.html`
    """
    login_url = "login"

    model = BacklogItem

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemAnimeAdd(LoginRequiredMixin, CreateView):
    """
    Display a form to add an item to backlog, from existing anime.
    Template:`backlog_manager/backlogitem_form.html`
    """
    login_url = "login"

    model = BacklogItem
    fields = ["anime", "status"]

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})

    def form_valid(self, form):
        # Save plan id to database
        form.instance.plan = Backlog.objects.get(pk=self.kwargs.get('backlog_pk'))
        # Gives next available order
        plan = self.kwargs["backlog_pk"]
        status = form.instance.status
        backlog_items = BacklogItem.objects.filter(plan=plan).filter(status=status).order_by("order")
        next_order = 1
        for item in backlog_items:
            next_order += 1
        form.instance.order = next_order
        return super().form_valid(form)


class BacklogItemAnimeUpdate(LoginRequiredMixin, UpdateView):
    """
    Display a form to update an anime entry in the backlog.
    Template:`backlog_manager/backlogitem_update_form.html`
    """
    login_url = "login"

    model = BacklogItem
    fields = ["anime", "order", "status"]
    template_name_suffix = "_update_form"

    def form_valid(self, form):
        plan = self.kwargs["backlog_pk"]
        status = form.instance.status
        backlog_items = list(BacklogItem.objects.filter(plan=plan).filter(status=status).order_by("order"))
        next_order = 1
        for item in backlog_items:
            if next_order == form.cleaned_data["order"]:
                next_order += 1
            item.order = next_order
            next_order += 1
        BacklogItem.objects.bulk_update(backlog_items, ["order"])
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemAnimeDelete(LoginRequiredMixin, DeleteView):
    """
    Display a confirmation to delete an anime entry in the backlog.
    Template:`backlog_manager/backlogitem_confirm_delete.html`
    """
    login_url = "login"

    model = BacklogItem

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemMovieTVAdd(LoginRequiredMixin, CreateView):
    """
    Display a form to add an item to backlog, from existing movie and tv series.
    Template:`backlog_manager/backlogitem_form.html`
    """
    login_url = "login"

    model = BacklogItem
    fields = ["movie_tv", "status"]

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})

    def form_valid(self, form):
        # Save plan id to database
        form.instance.plan = Backlog.objects.get(pk=self.kwargs.get('backlog_pk'))
        # Gives next available order
        plan = self.kwargs["backlog_pk"]
        status = form.instance.status
        backlog_items = BacklogItem.objects.filter(plan=plan).filter(status=status).order_by("order")
        next_order = 1
        for item in backlog_items:
            next_order += 1
        form.instance.order = next_order
        return super().form_valid(form)


class BacklogItemMovieTVUpdate(LoginRequiredMixin, UpdateView):
    """
    Display a form to update a movie or tv series entry in the backlog.
    Template:`backlog_manager/backlogitem_update_form.html`
    """
    login_url = "login"

    model = BacklogItem
    fields = ["movie_tv", "order", "status"]
    template_name_suffix = "_update_form"

    def form_valid(self, form):
        plan = self.kwargs["backlog_pk"]
        status = form.instance.status
        backlog_items = list(BacklogItem.objects.filter(plan=plan).filter(status=status).order_by("order"))
        next_order = 1
        for item in backlog_items:
            if next_order == form.cleaned_data["order"]:
                next_order += 1
            item.order = next_order
            next_order += 1
        BacklogItem.objects.bulk_update(backlog_items, ["order"])
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemMovieTVDelete(LoginRequiredMixin, DeleteView):
    """
    Display a confirmation to delete a movie or tv series entry in the backlog.
    Template:`backlog_manager/backlogitem_confirm_delete.html`
    """
    login_url = "login"

    model = BacklogItem

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemBookAdd(LoginRequiredMixin, CreateView):
    """
    Display a form to add an item to backlog, from existing books.
    Template:`backlog_manager/backlogitem_form.html`
    """
    login_url = "login"

    model = BacklogItem
    fields = ["book", "status"]

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})

    def form_valid(self, form):
        # Save plan id to database
        form.instance.plan = Backlog.objects.get(pk=self.kwargs.get('backlog_pk'))
        # Gives next available order
        plan = self.kwargs["backlog_pk"]
        status = form.instance.status
        backlog_items = BacklogItem.objects.filter(plan=plan).filter(status=status).order_by("order")
        next_order = 1
        for item in backlog_items:
            next_order += 1
        form.instance.order = next_order
        return super().form_valid(form)


class BacklogItemBookUpdate(LoginRequiredMixin, UpdateView):
    """
    Display a form to update a book entry in the backlog.
    Template:`backlog_manager/backlogitem_update_form.html`
    """
    login_url = "login"

    model = BacklogItem
    fields = ["book", "order", "status"]
    template_name_suffix = "_update_form"

    def form_valid(self, form):
        plan = self.kwargs["backlog_pk"]
        status = form.instance.status
        backlog_items = list(BacklogItem.objects.filter(plan=plan).filter(status=status).order_by("order"))
        next_order = 1
        for item in backlog_items:
            if next_order == form.cleaned_data["order"]:
                next_order += 1
            item.order = next_order
            next_order += 1
        BacklogItem.objects.bulk_update(backlog_items, ["order"])
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemBookDelete(LoginRequiredMixin, DeleteView):
    """
    Display a confirmation to delete a book entry in the backlog.
    Template:`backlog_manager/backlogitem_confirm_delete.html`
    """
    login_url = "login"

    model = BacklogItem

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})
