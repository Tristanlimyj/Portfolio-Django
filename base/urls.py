# Required Functions
from django.urls import path
import os
# URL & Views
from django.contrib import admin
from .admin import two_FA_admin
from .views import HomeView

urlpatterns = [
    path('', HomeView, name='home'),
]

# Type of Login
if os.getenv('SETTING_TYPE') == "Development":
    urlpatterns.append(path('admin/', admin.site.urls))
else:
     urlpatterns.append(path('admin/', two_FA_admin.urls)),