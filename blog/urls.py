from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('', include('base.urls')),
    path('admin/', admin.site.urls),
    path('posts/', include('post.urls')),
    path('projects/', include('project.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)