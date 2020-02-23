from django.shortcuts import render
from django.views.generic.base import TemplateView
from product.models import Category

# Create your views here.

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all() 
        return context