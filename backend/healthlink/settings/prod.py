"""Production settings"""

from .base import *  # noqa
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Cors settings
cors_allowed_origins = os.environ.get("CORS_ALLOWED_ORIGINS", "")
if cors_allowed_origins:
    CORS_ALLOWED_ORIGINS = cors_allowed_origins.split(",")
else:
    CORS_ALLOW_ALL_ORIGINS = True

# Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("EMAIL_HOST_USER")
EMAIL_USE_TLS = True

# Rest Framework settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
}

# Celery Configuration
CELERY_TIMEZONE = TIME_ZONE  # noqa
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")

# Cache settings
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": os.environ.get("REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}
