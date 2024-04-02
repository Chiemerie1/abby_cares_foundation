from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator
from .models import MainHeroSectionImage, NewsAndUpdate, NewMajorOutreach

# Create your views here.


def home(request):

    hero_image = MainHeroSectionImage.objects.last()
    news_and_update = NewsAndUpdate.objects.all()
    major_outreach = NewMajorOutreach.objects.last()
    last_three_blogs = Blog.objects.all().order_by("-id")[:3]


    return render(
        request=request,
        template_name="main/home.html",
        context={
            "hero_image": hero_image,
            "news_and_update": news_and_update,
            "major_outreach": major_outreach,
            "last_three_blogs": last_three_blogs
        }
    )


def blogs(request):

    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 12)

    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="main/blog.html",
        context={
            "css_image_url": "/static/img/BG8_4820.jpg",
            "page_object": page_object,
            "blogs": blogs
        }
        
    )


def blog_details(request, id):
    blog = Blog.objects.get(id=id)

    return render(
        request=request,
        template_name="main/blog_details.html",
        context={
            "blog": blog
        }
        
    )


def outreach(request):
    outreach = NewMajorOutreach.objects.all()
    paginator = Paginator(outreach, 12)

    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="main/outreach.html",
        context={
            "page_object": page_object,
        }
        
    )