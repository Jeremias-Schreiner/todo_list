from .models import Task
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True 

    def get_success_url(self) -> str:
        return reverse_lazy('task-list')  

class RegisterFormView(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
                login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task-list')
        return super().get(self, *args, **kwargs)

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/task-list.html'
    #queryset = Task.objects.all().order_by('title')

    def get_context_data(self, **kwargs):
        #Filter current user taks
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area','')

        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains = search_input
            )
        
        context['search_input'] = search_input

        return context

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task-detail.html'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    success_url = reverse_lazy('task-list')
    template_name = 'base/task-form.html'
    fields = ['title', 'description','complete']
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super(TaskCreateView, self).form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description','complete']
    success_url = reverse_lazy('task-list')
    template_name = 'base/task-form.html'

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task-list')
    template_name = 'base/task-delete.html'
