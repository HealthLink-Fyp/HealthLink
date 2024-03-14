from django.urls import path

from patient.views.search import AutoCompleteDoctorView

urlpatterns = [
    path("autocomplete/", AutoCompleteDoctorView.as_view(), name="search"),
]
