"""Development settings"""

from .base import *  # noqa

DEBUG = True

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Quick and dirty way to enable all hosts for development
ALLOWED_HOSTS = ["*"]

# URLs for frontend and backend
# if os.environ.get("CODESPACES") == "true":  # noqa
#     CODESPACE_NAME = os.environ.get("CODESPACE_NAME", "")  # noqa
#     CODESPACE_DOMAIN = os.environ.get("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN", "")  # noqa
#     BACKEND_URL = f"https://{CODESPACE_NAME}-8000.{CODESPACE_DOMAIN}"
#     FRONTEND_URL = f"https://{CODESPACE_NAME}-4200.{CODESPACE_DOMAIN}"
# else:
#     BACKEND_URL = "http://localhost:8000"
#     FRONTEND_URL = "http://localhost:4200"

# Variables
JWT_REFRESH_SECRET = "secret"
JWT_ACCESS_SECRET = "secret"
JWT_ACCESS_EXPIRE = 60 * 60 * 24 * 7  # 1 week
JWT_REFRESH_EXPIRE = 60 * 60 * 24 * 14  # 2 weeks

# Only show emails in console don't send it to smtp
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Cache settings
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}


# Rest Framework settings
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "EXCEPTION_HANDLER": "healthlink.utils.exceptions.custom_exception_handler",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}

# Spectacular settings
SPECTACULAR_SETTINGS = {
    "TITLE": "HealthLink API",
    "DESCRIPTION": "API for HealthLink",
    "VERSION": "1.0.0",
    "SCHEMA_PATH_PREFIX": "/api/v1",
    "SERVE_INCLUDE_SCHEMA": False,
    "SERVE_URLCONF": "healthlink.urls",
}

# Timezone for pakistan
TIME_ZONE = "Asia/Karachi"


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa
    }
}
