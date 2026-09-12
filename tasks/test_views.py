import pytest
from unittest.mock import patch
from django.urls import reverse
from rest_framework import status
from .models import Task

@pytest.mark.django_db
def test_task_list_view(client):
    response = client.get(reverse('task_list'))
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_task_create(client):
    response = client.post(reverse('task_create'), {
        'title': 'Task title',
        'descripion': 'Task description'
    })
    assert response.status_code == status.HTTP_302_FOUND

@pytest.mark.django_db
@patch('tasks.views.improve_task_description')
def test_improve_test_description(mocke_improve, client):
    improved_task_description = 'Improved task description'
    mock_improve.return_value = improved_task_description
    task = Task.objects.create(title='Task title', description='Task description')
    response = client.post(reverse('improve', args=[task.id]))
    task.refresh_from_db()
    assert task.description == improved_task_description
    assert response.status_code == status.HTTP_302_FOUND