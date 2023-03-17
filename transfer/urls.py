from django.urls import path
from . import views

urlpatterns = [
    path('', views.transfers),
    path('to-card/', views.transferToCard),
    path('to-phone/', views.transferToPhone),
    path('to-iban/', views.transferToIban),
]
