from django.urls import path
from .views import task_list, task_create, task_improve_description, task_delete, task_edit

urlpatterns = [
    path('', task_list, name='task_list'),
    path('new/', task_create, name='task_create'),
    path('<int:task_id>/improve/', task_improve_description, name='improve'),
    path('<int:task_id>/delete/', task_delete, name='delete'),
    path('<int:task_id>/edit/', task_edit, name='edit')
]