from django.contrib import admin
from base.admin import two_FA_admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_stamp')
    list_filter = ("time_stamp",)

admin.site.register(Project, ProjectAdmin)
two_FA_admin.register(Project, ProjectAdmin)