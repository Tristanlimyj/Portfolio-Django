from django.urls import path
from .views import AllProjectsView, ProjectDetailView

urlpatterns = [
    path('', AllProjectsView.as_view(), name='projects'),
    path('<str:title>', ProjectDetailView.as_view(), name='indv_project'),
]
