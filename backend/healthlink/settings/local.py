"""Development settings"""

from .base import *  # noqa

DEBUG = True

# Only show emails in console don't send it to smtp
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Cache settings
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

# Quick and dirty way to enable all hosts for development
ALLOWED_HOSTS = ["*"]

# Rest Framework settings
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": {
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.CursorPagination",
        "PAGE_SIZE": 10,
    },
}
