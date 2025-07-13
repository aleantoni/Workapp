from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/index.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'tasks/delete_task.html', {'task': task})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'tasks/register.html', {'form': form})

@csrf_exempt
@login_required
def toggle_task_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task_id = data.get('task_id')
        task = get_object_or_404(Task, id=task_id, user=request.user)
        
        # Alternar estado
        if task.status == 'P':
            task.status = 'C'
        else:
            task.status = 'P'
        
        task.save()
        return JsonResponse({'success': True, 
            'new_status': task.status, 
            'display_status': task.get_status_display()
            })
    
    return JsonResponse({'success': False}, status=400)        


# Create your views here.
