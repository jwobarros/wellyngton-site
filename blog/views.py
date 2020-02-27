from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from blog.models import Post

from watson import search as watson

# Create your views here.

class HomePageBlogView(ListView):
    template_name = "blog/home.html"
    model = Post
    ordering = ["-created_at"]
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            objects = self.model.objects.all()
        else:
            objects = self.model.objects.filter(public=True)

        search = self.request.GET.get('search', '')

        if search:
            objects = watson.filter(objects, search)

        return objects


def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    
    return render(request, template_name, {'post': post})