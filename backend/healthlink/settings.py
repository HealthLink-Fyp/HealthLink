"""Global Settings"""

# Python imports
import os
from pathlib import Path

import dj_database_url

# Third party imports
import dotenv

# Django imports
from django.core.management.utils import get_random_secret_key

dotenv.load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key
SECRET_KEY = os.environ.get("SECRET_KEY", get_random_secret_key())

# Frontend URL
FRONTEND_URL = os.environ.get("FRONTEND_URL", False)

# Email Settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("EMAIL_HOST_USER")
EMAIL_USE_TLS = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.getenv("DEBUG", 0)) == 1

# Allowed Hosts
ALLOWED_HOSTS = ["*"]

# Timezones
USE_TZ = True
TIME_ZONE = "UTC"

# CORS Settings
CORS_ALLOW_CREDENTIALS = True
# cors_allowed_origins = os.environ.get("CORS_ALLOWED_ORIGINS", "")
# if cors_allowed_origins:
#     CORS_ALLOWED_ORIGINS = cors_allowed_origins.split(",")

# else:
#     CORS_ALLOW_ALL_ORIGINS = True

# print(CORS_ALLOWED_ORIGINS)
CORS_ALLOWED_ORIGINS = ['https://curly-space-spork-7v95g6qq4r6whgj-4200.app.github.dev']
CORS_ALLOW_ALL_ORIGINS = True

# Application definition
INSTALLED_APPS = [
    # In-house apps
    "core",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-Party apps
    "corsheaders",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

# Rest Framework settings
# REST_FRAMEWORK = {
#     "DEFAULT_AUTHENTICATION_CLASSES": (
#         "rest_framework_simplejwt.authentication.JWTAuthentication",
#     ),
#     "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
#     "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
# }

# Django Auth Backend
AUTHENTICATION_BACKENDS = ("django.contrib.auth.backends.ModelBackend",)

# Cookie Settings
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Celery Configuration
CELERY_TIMEZONE = TIME_ZONE
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")

ROOT_URLCONF = "healthlink.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "healthlink.wsgi.application"


# Database
if bool(os.environ.get("DATABASE_URL")):
    DATABASES = {
        "default": dj_database_url.config(),
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "core.User"
