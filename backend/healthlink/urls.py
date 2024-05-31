from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

# index.html
from django.views.generic import TemplateView

from django.contrib.sites.models import Site

site = Site.objects.get_current()
current_site = site.domain


api_info = {
    "Status": "success",
    "Message": "Welcome to HealthLink API",
    "Version": "1.0.0",
}

urlpatterns = [
    path(
        "",
        TemplateView.as_view(
            template_name="index.html", extra_context={"api_info": api_info}
        ),
        name="index",
    ),
    path("admin/", admin.site.urls),
    path("api/v1/", include("core.urls")),
    path("api/v1/", include("patient.urls")),
    path("api/v1/", include("chat.urls")),
    # Add media photos path
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
