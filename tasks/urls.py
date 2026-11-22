from django.urls import path

from .views import (
    category_create,
    category_delete,
    category_edit,
    category_list,
    task_create,
    task_delete,
    task_edit,
    task_improve_description,
    task_list,
)

urlpatterns = [
    path("", task_list, name="task_list"),
    path("new/", task_create, name="task_create"),
    path("<int:task_id>/improve/", task_improve_description, name="improve"),
    path("<int:task_id>/delete/", task_delete, name="delete"),
    path("<int:task_id>/edit/", task_edit, name="edit"),
    path("categories/", category_list, name="category_list"),
    path("categories/new/", category_create, name="category_create"),
    path(
        "categories/<int:category_id>/delete/", category_delete, name="category_delete"
    ),
    path("categories/<int:category_id>/edit/", category_edit, name="category_edit"),
]
