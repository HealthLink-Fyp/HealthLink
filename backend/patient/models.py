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
    end = models.DateTimeField(null=True, blank=True, default=None)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.doctor.full_name}"
