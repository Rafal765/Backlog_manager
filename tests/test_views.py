from django.test import TestCase
import pytest
from backlog_manager.models import Genre, GameGenre, Anime, Book, Game, MovieTV, Backlog, BacklogItem
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def authorized_client(client):
    user = User.objects.create_user(username="test", password="test")
    client.force_login(user)
    return client


@pytest.fixture
def new_backlog(authorized_client):
    user_id = User.objects.get()
    new_backlog = Backlog.objects.create(name="test", user_id=user_id.pk)
    return new_backlog


@pytest.fixture
def game_genre():
    game_genre = GameGenre.objects.create(genre="example")
    return game_genre


@pytest.fixture
def game():
    game = Game.objects.create(title="game", comment="comment")
    return game


@pytest.mark.django_db
def test_game_create_unauthorized(game_genre, client):
    context = {
        "title": "Heroes 3",
        "comment": "regrehe",
        "genre": game_genre.pk,
    }
    count = Game.objects.count()
    response = client.post(reverse("game_create"), context)
    assert response.status_code == 302
    assert Game.objects.count() == count


@pytest.mark.django_db
def test_game_create_authorized(game_genre, authorized_client):
    context = {
        "title": "Heroes 3",
        "comment": "regrehe",
        "genre": game_genre.pk,
    }
    count = Game.objects.count()
    response = authorized_client.post(reverse("game_create"), context)
    assert response.status_code == 302
    assert Game.objects.count() == count + 1


@pytest.mark.django_db
def test_game_update_authorized(game, game_genre, authorized_client):
    context = {
        "title": "Heroes 3",
        "comment": "regrehe",
        "genre": game_genre.pk,
    }
    response = authorized_client.post(reverse("game_update", kwargs={"pk": game.id}), context)
    assert response.status_code == 302


@pytest.mark.django_db
def test_game_delete_authorized(game, authorized_client):
    response = authorized_client.post(reverse("game_delete", kwargs={"pk": game.id}))
    assert response.status_code == 302


@pytest.mark.django_db
def test_game_view_authorized(authorized_client):
    response = authorized_client.get(reverse("game"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_game_detail_view_authorized(game, authorized_client):
    response = authorized_client.get(reverse("game_detail", kwargs={"pk": game.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_backlog_create_authorized(authorized_client):
    context = {
        "name": "test",
    }
    count = Backlog.objects.count()
    response = authorized_client.post(reverse("backlog_create"), context)
    assert response.status_code == 302
    assert Backlog.objects.count() == count + 1


@pytest.mark.django_db
def test_backlog_view_proper_url_authorized(new_backlog, authorized_client):
    response = authorized_client.get(reverse("backlog", kwargs={"pk": new_backlog.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_backlog_view_proper_url_authorized(new_backlog, authorized_client):
    response = authorized_client.get(reverse("backlog", kwargs={"pk": new_backlog.pk}))
    assert response.status_code == 200


@pytest.mark.django_db
def test_backlog_view_add_game_authorized(game, new_backlog, authorized_client):
    context = {
        "game": game.pk,
        "status": "p",
    }
    count = BacklogItem.objects.count()
    response = authorized_client.post(reverse("backlog_game_create", kwargs={"backlog_pk": new_backlog.pk}), context)
    assert response.status_code == 302
    assert BacklogItem.objects.count() == count + 1


@pytest.mark.django_db
def test_backlog_view_update_game_authorized(game, new_backlog, authorized_client):
    context = {
        "game": game.pk,
        "status": "d",
        "order": 1,
    }
    response = authorized_client.post(reverse("backlog_game_create", kwargs={"backlog_pk": new_backlog.pk}), context)
    assert response.status_code == 302


#def test_should_check_password(db) -> None:
#    user = User.objects.create_user("A")
#    user.set_password("secret")
#    assert user.check_password("secret") is True



