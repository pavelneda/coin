from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("Main page")


def about(request):
    return HttpResponse("about page")


def depatments(request):
    return HttpResponse("depatments page")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")