from django.db import models
from core.models import PatientProfile, DoctorProfile


class Call(models.Model):
    call_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(
        PatientProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    doctor = models.ForeignKey(
        DoctorProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    peer_id = models.CharField(max_length=100)
    call_date = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)


class LLMResponse(models.Model):
    response_id = models.AutoField(primary_key=True)
    call = models.ForeignKey(Call, on_delete=models.CASCADE)
    transcription = models.TextField()
    response = models.JSONField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
