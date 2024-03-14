from core.models import DoctorProfile
from core.serializers import DoctorSearchBarSerializer

from rest_framework import filters
from rest_framework import generics


class AutoCompleteDoctorView(generics.ListAPIView):
    """
    View to return suggestions for doctor's city and specialization
    """

    serializer_class = DoctorSearchBarSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ("^city", "^specialization")

    def get_queryset(self):
        queryset = DoctorProfile.objects.only(
            "user", "city", "specialization", "profile_photo_url"
        )
        city = self.request.query_params.get("city", None)
        specialization = self.request.query_params.get("specialization", None)
        if city:
            queryset = queryset.filter(specialization__icontains=city)
        if specialization:
            queryset = queryset.filter(specialization__icontains=specialization)
        return queryset
