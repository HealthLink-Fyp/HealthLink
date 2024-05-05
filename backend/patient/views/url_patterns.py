from django.urls import path

from .search import SearchDoctorView, AutoCompleteDoctorView, DoctorDetailView
from .appointment import AppointmentView
from .records import MedicalRecordView
from .medicine import MedicineListView
from .medical_test import MedicalTestListView

appointment_patterns = [
    path("", AppointmentView.as_view(), name="appointment"),
    path("<int:appointment_id>/", AppointmentView.as_view(), name="appointment-detail"),
]

doctor_patterns = [
    path("<int:pk>/", DoctorDetailView.as_view(), name="doctor-detail"),
]

search_patterns = [
    path("doctors/", SearchDoctorView.as_view(), name="search-doctors"),
    path(
        "doctors/autocomplete/",
        AutoCompleteDoctorView.as_view(),
        name="autocomplete-doctors",
    ),
]

record_patterns = [
    path("", MedicalRecordView.as_view(), name="medical-record"),
    path("<int:pk>/", MedicalRecordView.as_view(), name="medical-record-detail"),
]


medicine_patterns = [
    path("", MedicineListView.as_view(), name="medicine-shop"),
    path("<int:medicine_id>/", MedicineListView.as_view(), name="medicine-shop-detail"),
]

medical_test_patterns = [
    path("", MedicalTestListView.as_view(), name="medical-test"),
    path("<int:test_id>/", MedicalTestListView.as_view(), name="medical-test-detail"),
]
