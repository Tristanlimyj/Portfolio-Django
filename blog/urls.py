from django.urls import include, path, re_path
from django.conf import settings
from django.conf.urls.static import static
import os

urlpatterns = [
    path('', include('base.urls')),
    path('posts/', include('post.urls')),
    path('projects/', include('project.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
