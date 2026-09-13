import pytest
from django.contrib.auth.models import User

@pytest.fixture
def user_init():
    user = User.objects.create_user(username='testuser', password='testpass123')
    return user

@pytest.fixture
def authenticated_client(user_init, client):
    client.login(username='testuser', password='testpass123')
    client.user = user_init
    return client

