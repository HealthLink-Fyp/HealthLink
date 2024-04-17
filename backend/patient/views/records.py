from patient.models import MedicalRecord
from patient.serializers import MedicalRecordSerializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from core.authentication import JWTAuthentication
from core.permissions import IsHealthcareProvider


class MedicalRecordView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete a MedicalRecord object.
    """

    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsHealthcareProvider]
    lookup_field = "pk"

    def get_queryset(self):
        """
        Get the queryset based on the user role.
        """

        if self.request.user.role == "patient":
            return MedicalRecord.objects.filter(patient=self.request.user.patient)
        elif self.request.user.role == "doctor":
            return MedicalRecord.objects.filter(doctor=self.request.user.doctor)
        elif self.request.user.role == "admin":
            return MedicalRecord.objects.all()
        return MedicalRecord.objects.none()

    def perform_create(self, serializer):
        """
        Create a MedicalRecord object.
        """

        serializer.save(patient=self.request.user.patient)

    def perform_update(self, serializer):
        """
        Update a MedicalRecord object.
        """

        serializer.save(patient=self.request.user.patient)

    def perform_destroy(self, instance):
        """
        Delete a MedicalRecord object.
        """

        instance.delete()

    def get(self, request, *args, **kwargs):
        """
        Get the MedicalRecord object based on the user role.
        """

        if "pk" in kwargs:
            self.object = self.get_object()
            return self.retrieve(request, *args, **kwargs)
        else:
            return super().get(request, *args, **kwargs)
