from core.models import DoctorProfile
from core.serializers import DoctorSearchBarSerializer
from rest_framework.response import Response

from rest_framework import filters
from rest_framework import generics


class AutoCompleteDoctorView(generics.ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorSearchBarSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ("^city", "^specialization", "^name")

    def get_queryset(self):
        specialization = self.request.query_params.get("specialization", None)

        queryset = DoctorProfile.objects.only(
            "user", "specialization", "city", "profile_photo_url"
        )

        if specialization:
            queryset = queryset.filter(specialization__icontains=specialization)
        return queryset
