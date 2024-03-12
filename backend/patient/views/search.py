from core.models import DoctorProfile
from core.serializers import DoctorProfileSerializer
from rest_framework.response import Response

from rest_framework import filters
from rest_framework import generics


class SearchDoctorView(generics.ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ("^city", "^specialization")

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {
                "results": serializer.data,
                "status": 200,
                "Data Length: ": len(serializer.data),
            }
        )
