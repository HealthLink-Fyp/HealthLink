from django.urls import path

from patient.views.search import (
    SearchDoctorView,
    AutoCompleteDoctorView,
    DoctorDetailView,
)

urlpatterns = [ 
    path("search/doctors/", SearchDoctorView.as_view(), name="search"),
    path("doctors/<int:pk>/", DoctorDetailView.as_view(), name="doctor-detail"),
    path(
        "search/doctors/autocomplete/",
        AutoCompleteDoctorView.as_view(),
        name="autocomplete",
    ),
]
