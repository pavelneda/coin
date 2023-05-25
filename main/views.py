from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from main.models import Department


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def departments(request):
    departments = Department.objects.all()
    return render(request, 'main/departments.html', {"departments": departments})

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")

