from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def depatments(request):
    return render(request, 'main/departments.html')

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")