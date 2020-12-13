from django.urls import path
from .views import HomeView, PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='indv_post'),
]