from celery import Celery
from plane.settings.redis import redis_instance

# Django settings for celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "plane.settings.production")

ri = redis_instance()

app = Celery("plane")

app.config_from_object("django.conf:settings", namespace="CELERY")