from django.urls import path
from .views import task_list, task_create, task_improve_description

urlpatterns = [
    path('', task_list, name='task_list'),
    path('new/', task_create, name='task_create'),
    path('<int:task_id>/improve/', task_improve_description, name='improve')
]