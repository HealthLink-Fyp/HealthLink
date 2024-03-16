from django.urls import path

from patient.views import search

urlpatterns = [
    path("search/doctors/", search.SearchDoctorView.as_view(), name="search"),
    path(
        "search/doctors/autocomplete/",
        search.AutoCompleteDoctorView.as_view(),
        name="autocomplete",
    ),
]
