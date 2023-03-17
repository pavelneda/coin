from django.urls import path

from . import views

urlpatterns = [
    path('', views.account),
    path('sign-in/', views.signIn),
    path('sign-up/', views.signUp),
]
