from django.shortcuts import render
from django.views.generic.list import ListView
from blog.models import Post

# Create your views here.

class HomePageBlogView(ListView):
    template_name = "blog/home.html"
    model = Post