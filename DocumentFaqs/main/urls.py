from django.contrib import admin
from . import settings
from django.conf.urls.static import static
from django.urls import path
from ninja import NinjaAPI
from docsFaqs.api import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
