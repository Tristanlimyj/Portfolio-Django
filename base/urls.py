from django.urls import path
from django.contrib import admin
from .admin import admin_site
from .views import HomeView

urlpatterns = [
    path('', HomeView, name='home'),
    path('admin/', admin.site.urls),
    path('dadmin/', admin_site.urls)
]