from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from base.models import Task

# Create your views here.

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/task-list.html'

class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task-detail.html'

class TaskCreateView(CreateView):
    model = Task
    success_url = reverse_lazy('task-list')
    template_name = 'base/task-form.html'
    fields = '__all__'