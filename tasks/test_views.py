import pytest
from django.contrib.auth.models import User
from unittest.mock import patch
from django.urls import reverse
from rest_framework import status
from .models import Task

@pytest.mark.django_db
def test_task_list_view(authenticated_client):
    response = authenticated_client.get(reverse('task_list'))
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_task_create(authenticated_client):
    task_title = 'Task title'
    task_description = 'Task description'
    response = authenticated_client.post(reverse('task_create'), {
        'title': task_title,
        'description': task_description
    })
    assert response.status_code == status.HTTP_302_FOUND
    task = Task.objects.get(title=task_title)
    assert task.description == task_description

@pytest.mark.django_db
@patch('tasks.views.improve_task_description')
def test_improve_test_description(mock_improve, authenticated_client):
    improved_task_description = 'Improved task description'
    mock_improve.return_value = improved_task_description
    task = Task.objects.create(title='Task title', description='Task description', owner=authenticated_client.user)
    response = authenticated_client.post(reverse('improve', args=[task.id]))
    task.refresh_from_db()
    assert task.description == improved_task_description
    assert response.status_code == status.HTTP_302_FOUND

@pytest.mark.django_db
def test_api_require_authorisation(client):
    response = client.get('/api/tasks/')
    assert response.status_code == status.HTTP_403_FORBIDDEN