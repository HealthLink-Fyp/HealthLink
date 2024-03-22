"""Development settings"""

from .base import *  # noqa

DEBUG = True

# Codespace Settings
# CODESPACE_NAME = os.environ.get("CODESPACE_NAME", "")  # noqa
# CODESPACE_PORT_DOMAIN = os.environ.get("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN", "")  # noqa
# BACKEND_URL = f"https://{CODESPACE_NAME}-8000.{CODESPACE_PORT_DOMAIN}"
# FRONTEND_URL = f"https://{CODESPACE_NAME}-4200.{CODESPACE_PORT_DOMAIN}"

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
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.CursorPagination",
    "PAGE_SIZE": 100,
}
