from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin): #campo de solo lectura 
    readonly_fields = ("create", )

# Register your models here.
admin.site.register(Task, TaskAdmin)