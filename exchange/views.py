from django.shortcuts import render
from django.http import HttpResponse


def exchange(request):
    return HttpResponse("exchange page")

