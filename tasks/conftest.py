import pytest
from django.contrib.auth.models import User
from .models import Task

@pytest.fixture
def user_init():
    user = User.objects.create_user(username='testuser', password='testpass123')
    return user

@pytest.fixture
def authenticated_client(user_init, client):
    client.login(username='testuser', password='testpass123')
    client.user = user_init
    return client

@pytest.fixture
def create_tasks(authenticated_client):
    def _create(amount):
        for i in range(amount):
            Task.objects.create(
                title=f'Task title {i}',
                description=f'Description for task #{i}',
                status='new',
                owner=authenticated_client.user
            )
    return _create