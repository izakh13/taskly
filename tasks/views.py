from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Category, Task
from .forms import TaskForm, StyledUserCreationForm, CategoryForm
from .services import improve_task_description
from .serializers import TaskSerializer

TASKS_PER_PAGE = 10

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

@login_required
def task_list(request):
    tasks = Task.objects.filter(owner=request.user).order_by('-created_at')
    paginator = Paginator(tasks, TASKS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_range = range(1, page_obj.paginator.num_pages+1)
    return render(request, 'tasks/task_list.html', {'page_obj': page_obj, 'page_range': page_range})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(user=request.user)
    return render(request, 'tasks/task_form.html', {'form': form, 'form_title': 'New task', 'form_button': 'Create'})

@login_required
def task_improve_description(request, task_id):
    task = Task.objects.filter(owner=request.user).get(id=task_id)
    task.description = improve_task_description(task.description)
    task.save()
    messages.success(request, 'Task updated successfully!')
    return redirect('task_list')

def register(request):
    if request.method == 'POST':
        form = StyledUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = StyledUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, owner=request.user, id=task_id)
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect('task_list')

@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, owner=request.user, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task, user=request.user)
    return render(request, 'tasks/task_form.html', {'form': form, 'form_title': f'Edit {task.title}', 'form_button': 'Save'})

@login_required
def category_list(request):
    tasks = Category.objects.filter(owner=request.user).order_by('-created_at')
    paginator = Paginator(tasks, TASKS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_range = range(1, page_obj.paginator.num_pages+1)
    return render(request, 'tasks/category_list.html', {'page_obj': page_obj, 'page_range': page_range})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, user=request.user)
        if form.is_valid():
            category = form.save(commit=False)
            category.owner = request.user
            category.save()
            messages.success(request, 'Category created successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm(user=request.user)
    return render(request, 'tasks/category_form.html', {'form': form, 'form_title': 'New category', 'form_button': 'Create'})

@login_required
def category_delete(request, category_id):
    category = get_object_or_404(Category, owner=request.user, id=category_id)
    category.delete()
    messages.success(request, 'Category deleted successfully!')
    return redirect('category_list')

@login_required
def category_edit(request, category_id):
    category = get_object_or_404(Category, owner=request.user, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category, user=request.user)
    return render(request, 'tasks/category_form.html', {'form': form, 'form_title': f'Edit {category.name}', 'form_button': 'Save'})
