from django.shortcuts import render
from django.http import HttpResponse


def transfers(request):
    return HttpResponse("transfers page")


def transferToCard(request):
    return HttpResponse("transfer To Card page")


def transferToPhone(request):
    return HttpResponse("transfer To Phone page")


def transferToIban(request):
    return HttpResponse("transfer To Iban page")
