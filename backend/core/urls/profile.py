from django.urls import path

from core.views.profile import (
    DoctorProfileView,
    PatientProfileView
)

urlpatterns = [
    path("doctor/", DoctorProfileView.as_view(), name="doctor"),
    path("patient/", PatientProfileView.as_view(), name="patient"),
]
