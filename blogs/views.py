from django.shortcuts import render
from django.http import HttpResponse

from blogs.models import Blog


def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/index.html', {"blogs": blogs})


def blog(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blogs/blog.html', {"blog": blog})


