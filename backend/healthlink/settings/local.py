"""Development settings"""

from .base import *  # noqa

DEBUG = True

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Quick and dirty way to enable all hosts for development
ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = ["https://organic-doodle-7v95g6qq45vwhr5wx-4200.app.github.dev"]
CORS_ORIGIN_WHITELIST = ["https://organic-doodle-7v95g6qq45vwhr5wx-4200.app.github.dev"]


# URLs for frontend and backend
# if os.environ.get("CODESPACES") == "true":  # noqa
#     CODESPACE_NAME = os.environ.get("CODESPACE_NAME", "")  # noqa
#     CODESPACE_DOMAIN = os.environ.get("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN", "")  # noqa
#     BACKEND_URL = f"https://{CODESPACE_NAME}-8000.{CODESPACE_DOMAIN}"
#     FRONTEND_URL = f"https://{CODESPACE_NAME}-4200.{CODESPACE_DOMAIN}"
# else:
#     BACKEND_URL = "http://localhost:8000"
#     FRONTEND_URL = "http://localhost:4200"

API_URL = "http://127.0.0.1:8000/"

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
    "EXCEPTION_HANDLER": "healthlink.utils.exceptions.custom_exception_handler",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
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
