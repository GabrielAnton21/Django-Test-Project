from django.shortcuts import render
from .forms import TaskForm


# Create your views here.
def index(request):
    return render(request, 'tasks/tasks.html')


def update_task(request):
    return render(request, 'tasks/update-form.html')


def delete_task(request):
    return render(request, 'tasks/delete-form.html')


def add_task(request):
    form = TaskForm()
    context = {'form': form}
    return render(request, 'tasks/add-form.html', context)


def complete_task(request):
    return render(request, 'tasks/complete-form.html')
