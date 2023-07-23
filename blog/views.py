from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView


class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/'




class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'blog/post_update.html'  # Optional: Specify the template to use
    success_url = '/'  # Optional: Redirect to this URL after successful update


class PostDelete(DeleteView):
    model = Post
    success_url = '/'

