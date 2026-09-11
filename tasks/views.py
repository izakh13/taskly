from rest_framework import viewsets
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from .services import improve_task_description
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
        return render(request, 'tasks/task_form.html', {'form': form})

def task_improve_description(request, task_id):
    task = Task.objects.get(id=task_id)
    task.description = improve_task_description(task.description)
    task.save()
    return redirect('task_list')
        