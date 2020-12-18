from django.urls import path
from .views import HomeView
from django.contrib.auth.views import LoginView
from django_otp.forms import OTPAuthenticationForm

urlpatterns = [
    path('', HomeView, name='home'),
]