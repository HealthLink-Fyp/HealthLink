from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    REQUIRED_FIELDS = []


class UserToken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField()


class UserForgot(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True)
