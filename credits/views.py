from django.shortcuts import render
from django.http import HttpResponse


def credits(request):
    return HttpResponse("credits page")

