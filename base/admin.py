from django.contrib import admin
from . models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['title', 'user', 'created', 'complete']
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title']
    list_filter = ['user']
    ordering = ['title']