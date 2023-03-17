from django.shortcuts import render
from django.http import HttpResponse


def account(request):
    return HttpResponse("account page")


def signIn(request):
    return HttpResponse("sign In page")


def signUp(request):
    return HttpResponse("sign Up page")
