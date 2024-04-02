
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from .import views



app_name="main"




urlpatterns = [
    path("", views.home, name="home"),
    path("blogs/", views.blogs , name="blogs"),
    path("blog_details/", views.blog_details , name="blog_details"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)