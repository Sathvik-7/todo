from django.contrib import admin
from .models import Task

#override the default admin interface
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'isCompleted', 'updatedAt')
    list_filter = ('isCompleted',)
    search_fields = ('task',)
    ordering = ('-createdAt',)

# Register your models here.
admin.site.register(Task, TaskAdmin)