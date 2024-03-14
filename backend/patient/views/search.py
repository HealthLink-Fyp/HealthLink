from core.models import DoctorProfile
from core.serializers import DoctorSearchBarSerializer

from rest_framework import filters
from rest_framework import generics


class AutoCompleteDoctorView(generics.ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorSearchBarSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ("^city", "^specialization")

    def get_queryset(self):
        specialization = self.request.query_params.get("specialization", None)
        city = self.request.query_params.get("city", None)

        queryset = DoctorProfile.objects.all()
        if specialization:
            queryset = queryset.filter(specialization__icontains=specialization)

        if city:
            queryset = queryset.filter(city__icontains=city)
        return queryset
