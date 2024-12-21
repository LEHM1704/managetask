from django.contrib import admin

from crud.models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['title','created']
    search_fields = ['title']
    ordering = ['-created']