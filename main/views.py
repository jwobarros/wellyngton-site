from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, Http404, HttpResponseRedirect
from product.models import Category
from blog.models import Post, Subscriber
# Create your views here.

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all() 
        context["posts"] = Post.objects.filter(public=True).order_by('-created_at')[:3]
        return context


@csrf_exempt
def subscribe_view(request):
    if request.method == "POST" and request.is_ajax():

        email = request.POST.get('email', None)
        if email:
            subscriber = Subscriber.objects.filter(email=email)
            
            if not subscriber.exists():
                Subscriber.objects.create(email=email)
            
            elif Subscriber.objects.get(email=email).active == False:
                Subscriber.objects.filter(email=email).update(active = True)   

            data = { 'registered': True }
            
            return JsonResponse(data)
    raise Http404("Página não encontrada.")