from django.urls import path
from .views import HomeView, PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='posts'),
    path('<str:title>', PostDetailView.as_view(), name='indv_post'),
]