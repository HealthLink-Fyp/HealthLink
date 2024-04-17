from core.models import DoctorProfile
from core.serializers import (
    DoctorAutoCompleteSerializer,
    DoctorSearchSerializer,
    DoctorProfileSerializer,
)

from rest_framework import filters
from rest_framework import generics


class AutoCompleteDoctorView(generics.ListAPIView):
    """
    API view to provide autocomplete functionality for DoctorProfile model.
    """

    serializer_class = DoctorAutoCompleteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ("^city", "^specialization")
    pagination_class = None

    def get_queryset(self):
        """
        Get the queryset for the view.
        """

        queryset = DoctorProfile.objects.only(
            "user", "full_name", "city", "specialization", "profile_photo_url"
        )
        return queryset


class SearchDoctorView(generics.ListAPIView):
    """
    API view to search for doctors based on city and specialization.
    """

    serializer_class = DoctorSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ("^city", "^specialization")
    # pagination_class = None

    def get_queryset(self):
        """
        Filter the Doctors based on city.
        """

        city = self.request.query_params.get("city", None)

        queryset = DoctorProfile.objects.only(
            "user",
            "full_name",
            "city",
            "specialization",
            "profile_photo_url",
            "patients_count",
            "reviews_count",
            "recommendation_percent",
            "consultation_fees",
            "wait_time",
            "experience_years",
        )

        if city:
            queryset = queryset.filter(city__icontains=city)

        return queryset


class DoctorDetailView(generics.RetrieveAPIView):
    """
    Get doctor profile by id.
    """

    serializer_class = DoctorProfileSerializer

    def get_queryset(self):
        """
        Get the Doctor profile based on the user id in the URL.
        """
        queryset = DoctorProfile.objects.filter(user=self.kwargs["pk"])
        return queryset
