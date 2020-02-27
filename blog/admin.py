from django.contrib import admin
from blog.models import Tag, Post, Subscriber
# Register your models here.

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Subscriber)