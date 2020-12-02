from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    form = TaskForm(request.POST or None)
    context = {'tasks': tasks, 'form': form}
    return render(request, 'Todo/index.html', context)


def add(request):
    form = TaskForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    return None


def delete(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'Todo/delete-confirm.html', {'task': task})


def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'Todo/update.html', {'form': form, 'task': task})


def complete(request, id):
    task = Task.objects.get(id=id)

    task.complete = True
    task.save()
    return redirect('index')
