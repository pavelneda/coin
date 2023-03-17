from django.shortcuts import render
from django.http import HttpResponse


def blogs(request):
    return HttpResponse("blogs page")


def blog(request, blog_id):
    return HttpResponse(f'{blog_id} blog page')

