from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("core.urls.authentication")),
    path("api/", include("core.urls.profile")),
    # Add media photos path
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
