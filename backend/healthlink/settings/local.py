"""Development settings"""

from .base import *  # noqa

DEBUG = True

# Codespace Settings
CODESPACE_NAME = os.environ.get("CODESPACE_NAME", "")  # noqa
CODESPACE_PORT_DOMAIN = os.environ.get("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN", "")  # noqa
BACKEND_URL = f"https://{CODESPACE_NAME}-8000.{CODESPACE_PORT_DOMAIN}"
FRONTEND_URL = f"https://{CODESPACE_NAME}-4200.{CODESPACE_PORT_DOMAIN}"

# Only show emails in console don't send it to smtp
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Cache settings
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

# CORS settings
CORS_ALLOWED_ORIGINS = [FRONTEND_URL]
# CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Quick and dirty way to enable all hosts for development
ALLOWED_HOSTS = [BACKEND_URL, FRONTEND_URL]

# Rest Framework settings
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": {
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.CursorPagination",
        "PAGE_SIZE": 10,
    },
}
