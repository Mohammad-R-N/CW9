from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Comment,Post


class BlogCommentView(ListView):

    model=Comment
    template_name='comment.html'


class BlogPostView(ListView):

    model=Post
    template_name='post.html'


class BlogDetailView(DetailView):
    model=Post
    template_name="detail.html"

def home_page(request):
    return render(request,"home.html")