from django.shortcuts import render
from django.views.generic import ListView
from .models import Author


class BlogAuthorView(ListView):

    model=Author
    template_name='index.html'