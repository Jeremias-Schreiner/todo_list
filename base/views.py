import imp
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from base.models import Task
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True 

    def get_success_url(self) -> str:
        return reverse_lazy('task-list')  

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/task-list.html'

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task-detail.html'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy('task-list')
    template_name = 'base/task-form.html'
    fields = '__all__'

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('task-list')
    template_name = 'base/task-form.html'

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')
    template_name = 'base/task-delete.html'
