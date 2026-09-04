import pytest
from datetime import datetime
from tasks.models import Task

@pytest.mark.django_db
def test_task_title():
    task = Task.objects.create(title='Buy milk')
    expected_title = 'Buy milk'
    assert task.title == expected_title

@pytest.mark.django_db
def test_default_values():
    task = Task.objects.create(title='Buy milk')
    expected_description = ''
    expected_done = False
    assert task.description == expected_description
    assert task.is_done == expected_done
    assert task.created_at is not None

@pytest.mark.django_db
def test_str_represantation():
    task = Task.objects.create(title='Buy milk')
    expected_str = f'Buy milk ({task.created_at.strftime("%d.%m.%Y %H:%M")})'
    assert str(task) == expected_str