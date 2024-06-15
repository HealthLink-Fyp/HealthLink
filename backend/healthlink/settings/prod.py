"""Production settings"""

from .base import *  # noqa
import os

import sentry_sdk


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.environ.get("DEBUG", False))

# Cors settings
cors_allowed_origins = os.environ.get("CORS_ALLOWED_ORIGINS", "")
if cors_allowed_origins:
    CORS_ALLOWED_ORIGINS = cors_allowed_origins.split(",")
else:
    CORS_ALLOW_ALL_ORIGINS = True

# Hosts settings
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",")
CORS_ORIGIN_WHITELIST = os.environ.get("CORS_ORIGIN_WHITELIST", "").split(",")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# JWT settings
JWT_REFRESH_SECRET = os.getenv("JWT_REFRESH_SECRET")
JWT_ACCESS_SECRET = os.getenv("JWT_ACCESS_SECRET")
JWT_ACCESS_EXPIRE = 60 * 60 * 24 * 7  # 1 week
JWT_REFRESH_EXPIRE = 60 * 60 * 24 * 14  # 2 weeks


# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("EMAIL_HOST_USER")
EMAIL_USE_TLS = True

# Cache settings
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.environ.get("REDIS_URL"),
        "OPTIONS": {
            "ssl_cert_reqs": None,
        },
    }
}


# Rest Framework settings
REST_FRAMEWORK = {
    "EXCEPTION_HANDLER": "healthlink.utils.exceptions.custom_exception_handler",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}

# Celery Configuration
# CELERY_TIMEZONE = TIME_ZONE  # noqa
# CELERY_TASK_SERIALIZER = "json"
# CELERY_ACCEPT_CONTENT = ["application/json"]
# CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")


# Timezone for pakistan
TIME_ZONE = "Asia/Karachi"

# Sentry Configuration
sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
