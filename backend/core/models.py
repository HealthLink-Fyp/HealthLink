from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

# Local Imports
from .choices import SPECIALIZATION_CHOICES, QUALIFICATION_CHOICES, ROLE_CHOICES

##------------- User Authentication Model --------------##

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, null=False, blank=False, default="patient")
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["first_name", "last_name", "username", "role"]
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


class UserToken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField()


class UserForgot(models.Model):
    email = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True)



##------------- Doctor Profile Model --------------##
    
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(max_length=255, choices=SPECIALIZATION_CHOICES, null=False, blank=False)
    qualification = models.CharField(max_length=255, choices=QUALIFICATION_CHOICES, null=False, blank=False)
    experience_years = models.IntegerField()
    city = models.CharField(max_length=255)
    available_timings = models.TimeField(null=True, blank=True)
    available_days = models.JSONField(null=True, blank=True)
    consultation_fees = models.IntegerField(null=False, blank=False)
    summary = models.TextField()
    wait_time = models.IntegerField(null=True, blank=True)
    recommendation_percent = models.IntegerField(null=True, blank=True)
    patients_count = models.IntegerField(null=True, blank=True)
    reviews_count = models.IntegerField(null=True, blank=True)
    profile_photo_url = models.ImageField(upload_to='doctor_profile_photos/', null=True, blank=True)

    def __str__(self):
        return (self.user.first_name + " " + self.user.last_name + " - " + self.user.email)


##------------- Patient Profile Model --------------##
    
class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=255, null=True, blank=True)
    blood_group = models.CharField(max_length=255, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    bmi = models.FloatField(null=True, blank=True)
    # Caluclate BMI and store it in the database
    def save(self, *args, **kwargs):
        if self.height and self.weight:
            self.bmi = self.weight / (self.height / 100) ** 2
        super().save(*args, **kwargs)
