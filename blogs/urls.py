from django.urls import path

from . import views

urlpatterns = [
    path('', views.blogs),
    path('<int:blog_id>/', views.blog),
]
