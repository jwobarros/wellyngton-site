from django.urls import path
from blog.views import HomePageBlogView, post_detail

urlpatterns = [
    path('', HomePageBlogView.as_view(), name='blog_home'),
    path('<slug:slug>/', post_detail, name='post-detail'),    
]