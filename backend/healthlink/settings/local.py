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

# Quick and dirty way to enable all hosts for development
ALLOWED_HOSTS = ["*"]