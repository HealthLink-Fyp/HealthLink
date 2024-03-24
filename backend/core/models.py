from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
import uuid

# Local Imports
from .choices import (
    SPECIALIZATION_CHOICES,
    QUALIFICATION_CHOICES,
    ROLE_CHOICES,
    DAY_CHOICES,
)


##------------- Base User Manager --------------##


class MyUserManager(BaseUserManager):
    """
    User manager class to create and manage the user.
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("role", "admin")

        user = self.create_user(email, password, **extra_fields)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True

        user.save(using=self._db)
        return user

    def create_doctor(self, email, password=None, **extra_fields):
        extra_fields.setdefault("role", "doctor")
        user = self.create_user(email, password, **extra_fields)
        return user

    def create_patient(self, email, password=None, **extra_fields):
        extra_fields.setdefault("role", "patient")
        user = self.create_user(email, password, **extra_fields)
        return user


##------------- User Authentication Model --------------##


class User(AbstractUser):
    """
    Model to store the user details.
    """

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, default="patient")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["role"]
    USERNAME_FIELD = "email"

    objects = MyUserManager()

    def is_admin(self):
        return self.role == "admin"

    def is_doctor(self):
        return self.role == "doctor"

    def is_patient(self):
        return self.role == "patient"

    def __str__(self):
        return f"{self.email} - {self.role}"


class UserToken(models.Model):
    """
    Model to store the JWT token for the user.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField()


class UserForgot(models.Model):
    """
    Model to store the email and token for password reset
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)


##------------- Doctor Profile Model --------------##


class DoctorProfile(models.Model):
    """
    Model to store the doctor profile details.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="doctor"
    )
    full_name = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    specialization = models.CharField(
        max_length=255, choices=SPECIALIZATION_CHOICES, db_index=True
    )
    qualification = models.CharField(
        max_length=255, choices=QUALIFICATION_CHOICES, db_index=True
    )
    experience_years = models.IntegerField()
    consultation_fees = models.IntegerField()
    summary = models.TextField(max_length=255)
    wait_time = models.IntegerField(null=True, blank=True, default=0)
    recommendation_percent = models.IntegerField(null=True, blank=True, default=0)
    patients_count = models.IntegerField(null=True, blank=True, default=0)
    reviews_count = models.IntegerField(null=True, blank=True, default=0)
    profile_photo_url = models.ImageField(
        null=True, blank=True, upload_to="profile_photos"
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def save(self, *args, **kwargs):
        self.full_name = f"{self.user.first_name} {self.user.last_name}"
        self.city = self.user.city
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} - {self.city}"


##------------- Availability Model --------------##


class Availability(models.Model):
    """
    Model to store the availability of a doctor.
    """

    doctor = models.ForeignKey(
        DoctorProfile, on_delete=models.CASCADE, related_name="availability_set"
    )
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor.full_name} - {self.day} - {self.start_time} to {self.end_time}"

    class Meta:
        unique_together = ["doctor", "day"]
        verbose_name_plural = "Availabilities"

    def save(self, *args, **kwargs):
        if self.start_time >= self.end_time:
            raise ValueError("End time must be greater than start time")
        super().save(*args, **kwargs)


##------------- Patient Profile Model --------------##


class PatientProfile(models.Model):
    """
    Model to store the patient profile details.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="patient"
    )
    full_name = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField()
    sex = models.BooleanField()
    blood_group = models.CharField(max_length=255)
    weight = models.IntegerField(default=1)
    height = models.IntegerField(default=1)
    bmi = models.FloatField(null=True, blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def save(self, *args, **kwargs):
        # Caluclate and store BMI it in the database
        H, W = self.height, self.weight
        self.bmi = round(W / ((H / 100) ** 2), 2)
        # Save name and city in the profile
        self.full_name = f"{self.user.first_name} {self.user.last_name}"
        self.city = self.user.city
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} - {self.city}"
