from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import HomePageView, subscribe_view

admin.site.site_header = 'Administração do site'
admin.site.index_title = ''
admin.site.site_title = 'Administração'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('subscribe', subscribe_view, name='subscribe'),
    path('blog/', include("blog.urls")),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
