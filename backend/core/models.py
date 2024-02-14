from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250, unique=True)
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)

    REQUIRED_FIELDS = []