from django.contrib import admin
from ../base/admin import admin_site
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_stamp')
    list_filter = ("time_stamp",)

admin.site.register(Project, ProjectAdmin)
admin_site.register(Project, ProjectAdmin)
