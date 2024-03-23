from core.models import PatientProfile, DoctorProfile
from core.choices import STATUS_CHOICES
from django.db import models


##------------- Appointment Model --------------##


class Appointment(models.Model):
    """
    Model to store the appointment details.
    """

    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")