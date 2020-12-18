from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_stamp')
    list_filter = ("time_stamp",)

admin.site.register(Project, ProjectAdmin)
