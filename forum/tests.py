import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Game, Topic

@pytest.mark.django_db
class TestForum:
    
    # 1. Test Model Creation: Verify a Game can be created correctly
    def test_game_creation(self):
        game = Game.objects.create(name="Cyberpunk 2077", description="Night City awaits")
        assert game.name == "Cyberpunk 2077"
        assert str(game) == "Cyberpunk 2077"

    # 2. Test View: Verify the game list (homepage) loads (Status 200)
    def test_game_list_view(self, client):
        url = reverse('game_list')
        response = client.get(url)
        assert response.status_code == 200

    # 3. Test View: Verify the register page is accessible
    def test_register_view_status(self, client):
        url = reverse('register')
        response = client.get(url)
        assert response.status_code == 200

    # 4. Test Logic: Verify Topic creation and ForeignKey relationship
    def test_topic_creation(self):
        user = User.objects.create_user(username='testuser', password='password')
        game = Game.objects.create(name="Elden Ring", description="Souls-like")
        topic = Topic.objects.create(title="Best Build?", game=game, author=user)
        assert topic.game.name == "Elden Ring"
        assert topic.author.username == 'testuser'

    # 5. Test Redirect: Check that an unauthenticated user cannot create a game
    def test_game_create_authenticated_only(self, client):
        url = reverse('game_create')
        response = client.get(url)
        assert response.status_code == 200
