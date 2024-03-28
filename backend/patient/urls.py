from django.urls import path

from patient.views import search, appointment

urlpatterns = [
    path("appointment/", appointment.AppointmentView.as_view(), name="appointment"),
    path(
        "appointment/<int:pk>",
        appointment.AppointmentView.as_view(),
        name="appointment-detail",
    ),
    path("search/doctors/", search.SearchDoctorView.as_view(), name="search"),
    path("doctors/<int:pk>/", search.DoctorDetailView.as_view(), name="doctor-detail"),
    path(
        "search/doctors/autocomplete/",
        search.AutoCompleteDoctorView.as_view(),
        name="autocomplete",
    ),
]
