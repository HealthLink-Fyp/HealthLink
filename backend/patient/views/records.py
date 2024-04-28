from patient.models import MedicalRecord
from patient.serializers import MedicalRecordSerializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from core.authentication import JWTAuthentication
from core.permissions import IsHealthcareProvider

from healthlink.utils.exceptions import (
    NotFound,
    ProfileNotFound,
    DoctorNotAllowed,
)


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

        user = self.request.user

        self.validate_user(user, method="get")

        roles = {
            "patient": lambda user: MedicalRecord.objects.filter(patient=user.patient),
            "doctor": lambda user: MedicalRecord.objects.filter(doctor=user.doctor),
        }

        return roles.get(user.role, lambda user: MedicalRecord.objects.none())(user)

    def perform_create(self, serializer):
        """
        Create a MedicalRecord object.
        """

        user = self.request.user
        self.validate_user(user)

        serializer.save(patient=user.patient)

    def perform_update(self, serializer):
        """
        Update a MedicalRecord object.
        """

        user = self.request.user
        self.validate_user(user)

        partial = self.request.method == "PATCH"

        serializer.save(patient=user.patient, partial=partial)

    def perform_destroy(self, instance):
        """
        Delete a MedicalRecord object.
        """

        self.validate_user(self.request.user)

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

    def validate_user(self, user, method=None):
        """
        Validate the user based on the user role.
        """

        # Check if the user exists
        if not user:
            raise NotFound("User")

        # Check if the user has a profile
        if user.role == "patient" and hasattr(user, "patient"):
            return
        elif user.role == "doctor" and hasattr(user, "doctor"):
            if method == "get":
                return
            raise DoctorNotAllowed("This Medical Record operation")
        else:
            raise ProfileNotFound()
