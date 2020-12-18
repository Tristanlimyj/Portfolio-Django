from django.contrib import admin
from base.admin import two_FA_admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_stamp')
    list_filter = ("time_stamp",)

admin.site.register(Post, PostAdmin)
two_FA_admin.register(Post, PostAdmin)
