from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Genre, GameGenre, Anime, Book, Game, MovieTV, Backlog, BacklogItem
#from .forms import BacklogItemGameUpdateForm, BacklogItemAnimeUpdateForm, \
 #   BacklogItemMovieTVUpdateForm, BacklogItemBookUpdateForm
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class MainView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        #user = Backlog.objects.filter(user__backlog=)
        ctx = {
        #    "user": user,
        }
        return render(request, "backlog_manager/my-backlogs.html", ctx)


class BacklogCreate(LoginRequiredMixin, CreateView):
    login_url = "login"

    model = Backlog
    fields = ["name"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("my_backlogs")


class BacklogUpdate(LoginRequiredMixin, UpdateView):
    login_url = "login"

    model = Backlog
    fields = ["name"]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy("my_backlogs")


class BacklogDelete(LoginRequiredMixin, DeleteView):
    login_url = "login"

    model = Backlog

    def get_success_url(self):
        return reverse_lazy("my_backlogs")


class BacklogView(LoginRequiredMixin, View):
    login_url = "login"

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


class GameView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        game_list = Game.objects.all().order_by('title')
        ctx = {
            'game_list': game_list,
        }
        return render(request, "backlog_manager/game-list.html", ctx)


class AnimeView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        anime_list = Anime.objects.all().order_by('title')
        ctx = {
            'anime_list': anime_list,
        }
        return render(request, "backlog_manager/anime-list.html", ctx)


class MovieTVView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        movie_tv_list = MovieTV.objects.all().order_by('title')
        ctx = {
            'movie_tv_list': movie_tv_list,
        }
        return render(request, "backlog_manager/movie-tv-list.html", ctx)


class BookView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        book_list = Book.objects.all().order_by('title')
        ctx = {
            'book_list': book_list,
        }
        return render(request, "backlog_manager/book-list.html", ctx)


class GenreView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        genre_list = Genre.objects.all().order_by('genre')
        ctx = {
            'genre_list': genre_list,
        }
        return render(request, "backlog_manager/genre-list.html", ctx)


class GameGenreView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request):
        game_genre_list = GameGenre.objects.all().order_by('genre')
        ctx = {
            'game_genre_list': game_genre_list,
        }
        return render(request, "backlog_manager/game-genre-list.html", ctx)


class GameDetailView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request, pk):
        game = Game.objects.get(pk=pk)
        ctx = {
            'game': game,
        }
        return render(request, "backlog_manager/game-detail.html", ctx)


class AnimeDetailView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request, pk):
        anime = Anime.objects.get(pk=pk)
        ctx = {
            'anime': anime,
        }
        return render(request, "backlog_manager/anime-detail.html", ctx)


class MovieTVDetailView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request, pk):
        movie_tv = MovieTV.objects.get(pk=pk)
        ctx = {
            'movie_tv': movie_tv,
        }
        return render(request, "backlog_manager/movie-tv-detail.html", ctx)


class BookDetailView(LoginRequiredMixin, View):
    login_url = "login"

    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        ctx = {
            'book': book,
        }
        return render(request, "backlog_manager/book-detail.html", ctx)


class GameCreate(LoginRequiredMixin, CreateView):
    login_url = "login"

    model = Game
    fields = ["title", "comment", "genre"]
    success_url = reverse_lazy("game")


class GameUpdate(LoginRequiredMixin, UpdateView):
    login_url = "login"

    model = Game
    fields = ["title", "comment", "genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("game")


class GameDelete(LoginRequiredMixin, DeleteView):
    login_url = "login"

    model = Game
    success_url = reverse_lazy("game")


class AnimeCreate(LoginRequiredMixin, CreateView):
    login_url = "login"

    model = Anime
    fields = ["title", "comment", "genre"]
    success_url = reverse_lazy("anime")


class AnimeUpdate(LoginRequiredMixin, UpdateView):
    login_url = "login"

    model = Anime
    fields = ["title", "comment", "genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("anime")


class AnimeDelete(LoginRequiredMixin, DeleteView):
    login_url = "login"

    model = Anime
    success_url = reverse_lazy("game")


class MovieTVCreate(LoginRequiredMixin, CreateView):
    login_url = "login"

    model = MovieTV
    fields = ["title", "comment", "genre"]
    success_url = reverse_lazy("movie_tv")


class MovieTVUpdate(LoginRequiredMixin, UpdateView):
    login_url = "login"

    model = MovieTV
    fields = ["title", "comment", "genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("movie_tv")


class MovieTVDelete(LoginRequiredMixin, DeleteView):
    login_url = "login"

    model = MovieTV
    success_url = reverse_lazy("movie_tv")


class BookCreate(LoginRequiredMixin, CreateView):
    login_url = "login"

    model = Book
    fields = ["title", "comment", "genre"]
    success_url = reverse_lazy("book")


class BookUpdate(LoginRequiredMixin, UpdateView):
    login_url = "login"

    model = Book
    fields = ["title", "comment", "genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("book")


class BookDelete(LoginRequiredMixin, DeleteView):
    login_url = "login"

    model = Book
    success_url = reverse_lazy("book")


class GameGenreCreate(LoginRequiredMixin, CreateView):
    login_url = "login"

    model = GameGenre
    fields = ["genre"]
    success_url = reverse_lazy("game_genre")


class GameGenreUpdate(LoginRequiredMixin, UpdateView):
    login_url = "login"

    model = GameGenre
    fields = ["genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("game_genre")


class GameGenreDelete(LoginRequiredMixin, DeleteView):
    login_url = "login"

    model = GameGenre
    success_url = reverse_lazy("game_genre")


class GenreCreate(LoginRequiredMixin, CreateView):
    login_url = "login"

    model = Genre
    fields = ["genre"]
    success_url = reverse_lazy("genre")


class GenreUpdate(LoginRequiredMixin, UpdateView):
    login_url = "login"

    model = Genre
    fields = ["genre"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("genre")


class GenreDelete(LoginRequiredMixin, DeleteView):
    login_url = "login"

    model = Genre
    success_url = reverse_lazy("genre")


class BacklogItemGameAdd(LoginRequiredMixin, CreateView):
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
            # item.save()
            next_order += 1
        form.instance.order = next_order
        return super().form_valid(form)


class BacklogItemGameUpdate(LoginRequiredMixin, UpdateView):
    login_url = "login"

    model = BacklogItem
    fields = ["game", "order", "status"]
    #form_class = BacklogItemGameUpdateForm
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
            #item.save()
            next_order += 1
        BacklogItem.objects.bulk_update(backlog_items, ["order"])
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemGameDelete(LoginRequiredMixin, DeleteView):
    login_url = "login"

    model = BacklogItem

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemAnimeAdd(LoginRequiredMixin, CreateView):
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
            # item.save()
            next_order += 1
        form.instance.order = next_order
        return super().form_valid(form)


class BacklogItemAnimeUpdate(LoginRequiredMixin, UpdateView):
    login_url = "login"

    model = BacklogItem
    fields = ["anime", "order", "status"]
    #form_class = BacklogItemAnimeUpdateForm
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
            #item.save()
            next_order += 1
        BacklogItem.objects.bulk_update(backlog_items, ["order"])
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemAnimeDelete(LoginRequiredMixin, DeleteView):
    login_url = "login"

    model = BacklogItem

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemMovieTVAdd(LoginRequiredMixin, CreateView):
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
            # item.save()
            next_order += 1
        form.instance.order = next_order
        return super().form_valid(form)


class BacklogItemMovieTVUpdate(LoginRequiredMixin, UpdateView):
    login_url = "login"

    model = BacklogItem
    fields = ["movie_tv", "order", "status"]
    # form_class = BacklogItemAnimeUpdateForm
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
            #item.save()
            next_order += 1
        BacklogItem.objects.bulk_update(backlog_items, ["order"])
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemMovieTVDelete(LoginRequiredMixin, DeleteView):
    login_url = "login"

    model = BacklogItem

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemBookAdd(LoginRequiredMixin, CreateView):
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
            # item.save()
            next_order += 1
        form.instance.order = next_order
        return super().form_valid(form)


class BacklogItemBookUpdate(LoginRequiredMixin, UpdateView):
    login_url = "login"

    model = BacklogItem
    fields = ["book", "order", "status"]
    # form_class = BacklogItemAnimeUpdateForm
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
            #item.save()
            next_order += 1
        BacklogItem.objects.bulk_update(backlog_items, ["order"])
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})


class BacklogItemBookDelete(LoginRequiredMixin, DeleteView):
    login_url = "login"

    model = BacklogItem

    def get_success_url(self):
        pk = self.kwargs["backlog_pk"]
        return reverse_lazy("backlog", kwargs={"pk": pk})
