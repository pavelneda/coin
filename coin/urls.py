from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from coin import settings
from main.views import pageNotFound

urlpatterns = [
    path('', include('main.urls')),
    path('blogs/', include('blogs.urls'), name="blogs"),
    path('account/', include('account.urls'), name="account"),
    path('transfer/', include('transfer.urls'), name="transfer"),
    path('deposits/', include('deposits.urls')),
    path('credits/', include('credits.urls'), name="credits"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
