"""Development settings"""

from .base import *  # noqa

DEBUG = True

# Codespace Settings
# CODESPACE_NAME = os.environ.get("CODESPACE_NAME", "")  # noqa
# CODESPACE_PORT_DOMAIN = os.environ.get("GITHUB_CODESPACES_PORT_FORWARDING_DOMAIN", "")  # noqa
# BACKEND_URL = f"https://{CODESPACE_NAME}-8000.{CODESPACE_PORT_DOMAIN}"
# FRONTEND_URL = f"https://{CODESPACE_NAME}-4200.{CODESPACE_PORT_DOMAIN}"

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
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.CursorPagination",
    "PAGE_SIZE": 100,
}
