# views.py
from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Task.objects.create(task=task)
    return redirect('index')

def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
    except Task.DoesNotExist:
        pass
    return redirect('index')

def mark_as_completed(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.completion_status = True
        task.save()
    except Task.DoesNotExist:
        pass
    return redirect('index')
