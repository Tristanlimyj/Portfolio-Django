from django.contrib import admin
from ../base/admin import admin_site
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_stamp')
    list_filter = ("time_stamp",)

admin.site.register(Post, PostAdmin)
admin_site.register(Post, PostAdmin)
