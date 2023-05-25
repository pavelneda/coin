from django.urls import path

from . import views

urlpatterns = [
    path('', views.account, name='account'),
    path('sign-in/', views.LoginUser.as_view(), name='signin'),
    path('sign-up/', views.RegisterUser.as_view(), name='signup'),
    path('logout', views.logout_user, name='logout'),
    path('transfer', views.transfer, name='transfer'),
    path('ajax-card', views.ajax_card, name='create-card')
]
