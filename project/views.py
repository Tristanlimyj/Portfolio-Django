from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project

class AllProjectsView(ListView):
    model = Project
    template_name = 'projects.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'indv_project.html'
