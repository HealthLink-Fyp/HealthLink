from core.models import DoctorProfile
from core.serializers import DoctorAutoCompleteSerializer, DoctorSearchSerializer

from rest_framework import filters
from rest_framework import generics


class AutoCompleteDoctorView(generics.ListAPIView):
    """
    View to return suggestions for doctor's city and specialization
    """

    serializer_class = DoctorAutoCompleteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ("^city", "^specialization")
    pagination_class = None

    def get_queryset(self):
        queryset = DoctorProfile.objects.only(
            "user", "full_name", "city", "specialization", "profile_photo_url"
        )
        return queryset


class SearchDoctorView(generics.ListAPIView):
    """
    View to search doctor
    """

    serializer_class = DoctorSearchSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ("^city", "^specialization")
    # pagination_class = None

    def get_queryset(self):
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
            "available_days",
        )

        if city:
            queryset = queryset.filter(city__icontains=city)

        return queryset
