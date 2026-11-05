import pytest
from django.contrib.auth.models import User
from unittest.mock import patch
from django.urls import reverse
from rest_framework import status
from .models import Task
from .views import TASKS_PER_PAGE

@pytest.mark.django_db
def test_task_list_view(authenticated_client):
    response = authenticated_client.get(reverse('task_list'))
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_task_create(authenticated_client):
    task_title = 'Task title'
    task_description = 'Task description'
    task_status = 'new'
    response = authenticated_client.post(reverse('task_create'), {
        'title': task_title,
        'description': task_description,
        'status': task_status
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

@pytest.mark.django_db
def test_delete(authenticated_client):
    task = Task.objects.create(title='Task title', description='Task description', owner=authenticated_client.user)
    response = authenticated_client.post(reverse('delete', args=[task.id]))
    assert not Task.objects.filter(id=task.id).exists()
    assert response.status_code == status.HTTP_302_FOUND

@pytest.mark.django_db
def test_edit(authenticated_client):
    task = Task.objects.create(title="Old title", description="Old description", status='new', owner=authenticated_client.user)
    response = authenticated_client.post(reverse('edit', args=[task.id]), {
        'title': 'New title',
        'description': 'New description',
        'status': 'in_progress'
    })
    assert response.status_code == status.HTTP_302_FOUND
    task.refresh_from_db()
    assert task.title == 'New title'
    assert task.description == 'New description'
    assert task.status == 'in_progress'

@pytest.mark.django_db
def test_pagination_first_page(authenticated_client, create_tasks):
    tasks = create_tasks(25)
    response = authenticated_client.get(reverse('task_list'))
    page_obj = response.context['page_obj']
    assert response.status_code == status.HTTP_200_OK
    assert len(page_obj) == TASKS_PER_PAGE

@pytest.mark.django_db
def test_pagination_has_next_page_first_page(authenticated_client, create_tasks):
    tasks = create_tasks(25)
    response = authenticated_client.get(reverse('task_list'))
    page_obj = response.context['page_obj']
    assert response.status_code == status.HTTP_200_OK
    assert page_obj.has_next() == True

@pytest.mark.django_db
def test_pagination_has_previous_page_on_first_page(authenticated_client, create_tasks):
    tasks = create_tasks(25)
    response = authenticated_client.get(reverse('task_list'))
    page_obj = response.context['page_obj']
    assert response.status_code == status.HTTP_200_OK
    assert page_obj.has_previous() == False

@pytest.mark.django_db
def test_pagination_has_next_page_second_page(authenticated_client, create_tasks):
    tasks = create_tasks(25)
    response = authenticated_client.get(reverse('task_list'), {'page': 2})
    page_obj = response.context['page_obj']
    assert response.status_code == status.HTTP_200_OK
    assert page_obj.has_next() == True

@pytest.mark.django_db
def test_pagination_has_previous_page_on_second_page(authenticated_client, create_tasks):
    tasks = create_tasks(25)
    response = authenticated_client.get(reverse('task_list'), {'page': 2})
    page_obj = response.context['page_obj']
    assert response.status_code == status.HTTP_200_OK
    assert page_obj.has_previous() == True

@pytest.mark.django_db
def test_pagination_has_previous_page_on_last_page(authenticated_client, create_tasks):
    TASK_AMOUNT = 25
    tasks = create_tasks(TASK_AMOUNT)
    import math
    response = authenticated_client.get(reverse('task_list'), {'page': math.ceil(TASK_AMOUNT/TASKS_PER_PAGE)})
    page_obj = response.context['page_obj']
    assert response.status_code == status.HTTP_200_OK
    assert page_obj.has_previous() == True

@pytest.mark.django_db
def test_pagination_has_next_page_on_last_page(authenticated_client, create_tasks):
    TASK_AMOUNT = 25
    tasks = create_tasks(TASK_AMOUNT)
    import math
    response = authenticated_client.get(reverse('task_list'), {'page': math.ceil(TASK_AMOUNT/TASKS_PER_PAGE)})
    page_obj = response.context['page_obj']
    assert response.status_code == status.HTTP_200_OK
    assert page_obj.has_next() == False

@pytest.mark.django_db
def test_pagination_tasks_amount_on_last_page(authenticated_client, create_tasks):
    TASK_AMOUNT = 25
    tasks = create_tasks(TASK_AMOUNT)
    import math
    response = authenticated_client.get(reverse('task_list'), {'page': math.ceil(TASK_AMOUNT/TASKS_PER_PAGE)})
    page_obj = response.context['page_obj']
    assert response.status_code == status.HTTP_200_OK
    assert len(page_obj) == 5