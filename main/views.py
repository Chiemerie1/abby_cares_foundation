from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    return render(request=request, template_name="main/home.html")


def blogs(request):

    # blogs = Blog.objects.all()
    # paginator = Paginator(blogs, 12)

    # page_number = request.GET.get("page")
    # page_object = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="main/blog.html",
        context={
            "css_image_url": "/static/img/BG8_4820.jpg"
            # "page_object": page_object,
            # "blogs": blogs
        }
        
    )


def blog_details(request, id):
    blog = Blog.objects.get(id=id)

    # return redirect("main:skillas_gigs_details", pk=gig)
    return render(
        request=request,
        template_name="main/blog_details.html",
        context={
            "blog": blog
        }
        
    )


def outreach(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 12)

    page_number = request.GET.get("page")
    page_object = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="main/outreach.html",
        context={
            "page_object": page_object,
        }
        
    )