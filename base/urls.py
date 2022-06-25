from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('', views.TaskListView.as_view(), name="task-list"),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task-create', views.TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('taks-delete/<int:pk>/', views.TaskDeleteView.as_view(), name="task-delete")
]