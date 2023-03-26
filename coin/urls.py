from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from coin import settings
from main.views import pageNotFound

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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
