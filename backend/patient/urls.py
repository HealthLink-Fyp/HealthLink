from django.urls import path, include

from patient.views.url_patterns import (
    appointment_patterns,
    doctor_patterns,
    search_patterns,
    record_patterns,
)

urlpatterns = [
    path("appointment/", include(appointment_patterns)),
    path("doctors/", include(doctor_patterns)),
    path("search/", include(search_patterns)),
    path("records/", include(record_patterns)),
]
