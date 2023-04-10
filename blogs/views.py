from django.shortcuts import render
from django.http import HttpResponse


def blogs(request):
    return render(request, 'blogs/index.html')


def blog(request, blog_id):
    return render(request, 'blogs/blog.html')

