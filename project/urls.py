from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("shipping/admin/", admin.site.urls),
    path("shipping/api/", include("company.urls")),
    path("shipping/api/", include("consumer.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
