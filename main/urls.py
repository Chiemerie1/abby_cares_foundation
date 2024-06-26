
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
    path("blog_details/<int:id>", views.blog_details , name="blog_details"),
    path("news_and_update/", views.news_and_update , name="news_and_update"),
    path("news_and_update_details/<int:id>", views.news_and_update_details , name="news_and_update_details"),
    path("about/", views.about , name="about"),
    path("leadership/", views.leadership , name="leadership"),
    path("ways_to_give/", views.ways_to_give , name="ways_to_give"),
    path("careers/", views.careers , name="careers"),
    path("donate/", views.donate , name="donate"),
    path("volunteers/", views.volunteers , name="volunteers"),
    path("focus_area/", views.focus_area , name="focus_area"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)