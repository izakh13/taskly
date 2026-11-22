import pytest
from django.test import Client
from pytest_django.fixtures import django_user_model
from django.contrib.auth.models import User
from .models import Task

@pytest.fixture
def user_init():
    user = User.objects.create_user(username='testuser', password='testpass123')
    return user

@pytest.fixture
def client_factory(django_user_model):
    def _create(username):
        _user = django_user_model.objects.create_user(username=username, password=None)
        client  = Client()
        client.force_login(user=_user)
        client.user = _user
        return client
    return _create

@pytest.fixture
def authenticated_client(client_factory):
    username = "testuser"
    client = client_factory(username=username)
    return client

@pytest.fixture
def multiple_authenticated_clients(client_factory):
    client = client_factory(username="testuser1")
    client1 = client_factory(username="testuser2")
    return (client, client1)

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
