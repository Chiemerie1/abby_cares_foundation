from django.shortcuts import redirect, render
from .models import Blog
from django.core.paginator import Paginator
from .models import MainHeroSectionImage, NewsAndUpdate, NewMajorOutreach
from .forms import VolunteerContactForm
from django.contrib import messages

# Create your views here.


def home(request):

    hero_image = MainHeroSectionImage.objects.last()
    news_and_update = NewsAndUpdate.objects.all().order_by("-id")[:3]
    major_outreach = NewMajorOutreach.objects.last()
    last_three_blogs = Blog.objects.all().order_by("-id")[:3]

    if request.method == "POST":
        form = VolunteerContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You information has been successfully submitted")
            return redirect("main:home")
            
    form = VolunteerContactForm()
    return render(
        request=request,
        template_name="main/home.html",
        context={
            "hero_image": hero_image,
            "news_and_update": news_and_update,
            "major_outreach": major_outreach,
            "last_three_blogs": last_three_blogs,
            "form": form
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


def news_and_update(request):

    news_and_update = NewsAndUpdate.objects.all()
    paginator = Paginator(news_and_update, 12)

    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="main/news_and_update.html",
        context={
            "css_image_url": "/static/img/BG8_4816.jpg",
            "page_object": page_object,
            "news_and_update": news_and_update,
        }
        
    )


def news_and_update_details(request, id):
    news_and_update = NewsAndUpdate.objects.get(id=id)

    return render(
        request=request,
        template_name="main/news_and_update_details.html",
        context={
            "news_and_update": news_and_update,
        }
        
    )


def about(request):

    return render(
        request=request,
        template_name="main/about.html",
        context={
            "css_image_url": "/static/img/BG8_4907.jpg",
        }
        
    )


def leadership(request):

    return render(
        request=request,
        template_name="main/leadership.html",
        context={

        }
        
    )


def donate(request):

    return render(
        request=request,
        template_name="main/donate.html",
        context={
            
        }
        
    )


def ways_to_give(request):

    return render(
        request=request,
        template_name="main/ways_to_give.html",
        context={
            "css_image_url": "/static/img/donate.jpg",
        }
        
    )


def careers(request):

    return render(
        request=request,
        template_name="main/careers.html",
        context={

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


def volunteers(request):

    if request.method == "POST":
        form = VolunteerContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You information has been successfully submitted")
            return redirect("main:volunteers")
    form = VolunteerContactForm()

    return render(
        request=request,
        template_name="main/volunteers.html",
        context={
            "css_image_url": "/static/img/donate.jpg",
                        "form": form

        }
        
    )



def focus_area(request):

    return render(
        request=request,
        template_name="main/focus_area.html",
        context={
            "css_image_url": "/static/img/donate.jpg",
        }
        
    )