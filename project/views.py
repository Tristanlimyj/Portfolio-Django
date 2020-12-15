from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project

class AllProjectsView(ListView):
    model = Project
    template_name = 'projects.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'indv_project.html'

    def get_object(self):
        return get_object_or_404(Project, title=self.kwargs['title'].replace('-', ' '))