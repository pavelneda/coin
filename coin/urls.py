from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('blogs/', include('blogs.urls')),
    path('account/', include('account.urls')),
    path('transfer/', include('transfer.urls')),
    path('deposits/', include('deposits.urls')),
    path('credits/', include('credits.urls')),
    path('exchange/', include('exchange.urls')),
    path('admin/', admin.site.urls),
]
