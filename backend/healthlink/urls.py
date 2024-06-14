from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("core.urls")),
    path("api/v1/", include("patient.urls")),
    path("api/v1/", include("chat.urls")),
]

urlpatterns += [
    path(
        "",
        TemplateView.as_view(
            template_name="index.html",
            extra_context={
                "api_info": {
                    "title": "HealthLink API",
                    "version": "1.0.0",
                    "uptime": "100%",
                    "db_connection": "OK",
                    "endpoint": "/api/v1/",
                    "authentication": "JWT",
                }
            },
        ),
        name="index",
    )
]
