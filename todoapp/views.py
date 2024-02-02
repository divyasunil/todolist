from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TaskForm
from .models import Task

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# //Generic Views
class Tasklistview(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'taskdetails'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapp:vdetail', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('todoapp:vhome')


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
