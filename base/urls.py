from django.urls import path
from django.contrib import admin
from .views import HomeView
from django.contrib.auth.views import LoginView
from django_otp.forms import OTPAuthenticationForm

urlpatterns = [
    path('', HomeView, name='home'),
    path('admin/', admin.site.urls),
    path('admin/login/', LoginView.as_view(
            authentication_form = OTPAuthenticationForm,
            template_name = "login.html",
        )
    ),
]