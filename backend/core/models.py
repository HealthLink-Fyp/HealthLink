from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Local Imports
from .choices import SPECIALIZATION_CHOICES, QUALIFICATION_CHOICES, ROLE_CHOICES

##------------- Base User Manager --------------##


class MyUserManager(BaseUserManager):
    def create_user(
        self,
        first_name,
        last_name,
        email,
        username,
        password,
        role,
        phone_number=None,
        address=None,
        city=None,
    ):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username,
            role=role,
            phone_number=phone_number,
            address=address,
            city=city,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None, role="admin"):
        user = self.create_user(
            first_name="admin",
            last_name="admin",
            email=email,
            username=username,
            password=password,
            role=role,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


##------------- User Authentication Model --------------##


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    username = models.CharField(max_length=255, unique=True, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    role = models.CharField(
        max_length=255, choices=ROLE_CHOICES, null=False, blank=False
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["username", "role"]
    USERNAME_FIELD = "email"

    objects = MyUserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class UserToken(models.Model):
    user_id = models.IntegerField()
    token = models.CharField(max_length=255, unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateTimeField()


class UserForgot(models.Model):
    email = models.EmailField(max_length=255, null=False, blank=False)
    token = models.CharField(max_length=255, null=False, blank=False)


##------------- Doctor Profile Model --------------##


class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialization = models.CharField(
        max_length=255, choices=SPECIALIZATION_CHOICES, null=False, blank=False
    )
    qualification = models.CharField(
        max_length=255, choices=QUALIFICATION_CHOICES, null=False, blank=False
    )
    experience_years = models.IntegerField()
    city = models.CharField(max_length=255)
    available_timings = models.TimeField(null=False, blank=False)
    available_days = models.JSONField(null=True, blank=True)
    consultation_fees = models.IntegerField(null=False, blank=False)
    summary = models.TextField(max_length=255, null=False, blank=False)
    wait_time = models.IntegerField(null=True, blank=True)
    recommendation_percent = models.IntegerField(null=True, blank=True)
    patients_count = models.IntegerField(null=True, blank=True) 
    reviews_count = models.IntegerField(null=True, blank=True)
    profile_photo_url = models.ImageField(null=True, blank=True)

    def __str__(self):
        return (
            self.user.first_name + " " + self.user.last_name + " - " + self.user.email
        )


##------------- Patient Profile Model --------------##


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(null=False, blank=False)
    sex = models.BooleanField(null=False, blank=False)
    blood_group = models.CharField(max_length=255, null=False, blank=False)
    weight = models.IntegerField(null=False, blank=False)
    height = models.IntegerField(null=False, blank=False)
    bmi = models.FloatField(null=True, blank=True)

    # Caluclate BMI and store it in the database
    def save(self, *args, **kwargs):
        if self.height and self.weight:
            self.bmi = self.weight / (self.height / 100) ** 2
        super().save(*args, **kwargs)

    def __str__(self):
        return (
            self.user.first_name + " " + self.user.last_name + " - " + self.user.email
        )
