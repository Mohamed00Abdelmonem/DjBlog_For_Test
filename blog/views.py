from django.shortcuts import render
from .models import Post, Comment
from django.views.generic import ListView


class PostList(ListView):
    model = Post

