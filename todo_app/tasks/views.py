from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django! Welcome to the To-Do App.")



def task_list_create(request):
    tasks = Task.objects.all().order_by('-created_at')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_list.html', {'form': form, 'tasks': tasks})


def task_list(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')

    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})

def mark_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('task-list')
