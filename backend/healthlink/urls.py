from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("core.urls.authentication")),
    path("api/profile/", include("core.urls.profile")),
]
