from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'posts.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'indv_post.html'

    def get_object(self):
        return get_object_or_404(Post, title=self.kwargs['title'].replace('-', ' '))
