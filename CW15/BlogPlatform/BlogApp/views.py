from django.shortcuts import render
from django.views.generic import ListView
from .models import Comment,Post


class BlogCommentView(ListView):

    model=Comment
    template_name='comment.html'


class BlogPostView(ListView):

    model=Post
    template_name='post.html'