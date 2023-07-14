from django.shortcuts import render
from django.views.generic import ListView
from .models import Category


class BlogCategoryView(ListView):

    model=Category
    template_name='index.html'