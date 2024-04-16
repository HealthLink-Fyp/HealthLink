from core.models import PatientProfile, DoctorProfile
from core.choices import APPOINTMENT_STATUS_CHOICES, PAYMENT_CHOICES
from django.db import models


##------------- Appointment Model --------------##


class Appointment(models.Model):
    """
    Model to store the appointment details.
    """

    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        PatientProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True, default=None)
    appointment_status = models.CharField(
        max_length=20, choices=APPOINTMENT_STATUS_CHOICES, default="pending"
    )
    payment_status = models.CharField(
        max_length=20, choices=PAYMENT_CHOICES, default="pending"
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.doctor.full_name}"


##------------- Medical Record Model --------------##


class MedicalRecord(models.Model):
    """
    Model to store the medical records of the patient.
    """

    record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    doctor_note = models.TextField()
    llm_note = models.TextField()
    prescription = models.FileField(upload_to="prescriptions/", null=True, blank=True)
    test_result = models.FileField(upload_to="test_results/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.doctor.full_name}"
