from django.shortcuts import render
from post.models import Post
from project.models import Project

# Create your views here.
def HomeView(request):
    posts = Post.objects.order_by('-time_stamp')[:3]
    projects = Project.objects.order_by('-time_stamp')[:3]
    values = {
        'posts' : posts,
        'projects': projects,
    }
    return render(request, 'home.html', context=values)
