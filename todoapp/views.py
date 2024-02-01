from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


# Create your views here.
def home(request):
    task_details = Task.objects.all()
    if request.method == "POST":
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect('/')
    return render(request, 'home.html', {'taskdetails': task_details})


def details(request):
    task_details = Task.objects.all()
    return render(request, 'details.html', {'taskdetails': task_details})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'task': task})
