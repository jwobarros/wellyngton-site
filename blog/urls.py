from django.urls import path
from blog.views import HomePageBlogView

urlpatterns = [
    path('', HomePageBlogView.as_view(), name='blog_home'),    
]