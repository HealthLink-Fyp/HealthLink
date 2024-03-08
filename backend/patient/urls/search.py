from django.urls import path

from patient.views.search import SearchDoctorView

urlpatterns = [
    path("autocomplete/", SearchDoctorView.as_view(), name="search"),
]
