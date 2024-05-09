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
    doctor_notes = models.TextField(null=True, blank=True)
    past_records = models.FileField(upload_to="past_records/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.patient.full_name} - {self.doctor.full_name}"


##------------- Medicine Shop Model --------------##


class MedicineShop(models.Model):
    """
    Model to store the medicine details of the shop.
    """

    medicine_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField()
    manufacturer = models.CharField(max_length=100)
    pack_details = models.CharField(max_length=100)
    image = models.URLField()
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name


##------------- Medical Test Model --------------##


class MedicalTest(models.Model):
    """
    Model to store the medical test details.
    """

    test_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField()
    lab_name = models.CharField(max_length=100, default="Chughtai Lab")
    image = models.URLField(
        default="https://pbs.twimg.com/profile_images/1522880282810015745/-Uax8id5_400x400.jpg"
    )
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.name
