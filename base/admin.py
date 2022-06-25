from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    search_fields = ['title']
    ordering = ['complete','title']

admin.site.register(Task, TaskAdmin)
