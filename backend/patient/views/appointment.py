# Python Imports
import datetime

# Django Imports
from django.db.models import Q
from django.utils import timezone

# Rest Framework Imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from healthlink.utils.exceptions import (
    DoctorNotAvailable,
    UnableToDestroyPastAppointment,
    ProfileNotFound,
    PastAppointment,
    DoctorAvailabilityNotFound,
    URLKwargNotFound,
)

# Local Imports
from core.models import DoctorProfile
from patient.models import Appointment
from patient.serializers import AppointmentSerializer
from healthlink.utils.response_handler import send_response
from core.authentication import JWTAuthentication


class AppointmentView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = None
    lookup_field = "appointment_id"

    def get_queryset(self):
        """
        Return the appointments of the user based on their role.
        """

        user = self.request.user
        appointment_id = self.kwargs.get("appointment_id", None)

        # Check if the user's patient or doctor profile exists
        if user.role == "patient" and hasattr(user, "patient"):
            queryset = Appointment.objects.filter(patient=user.patient)
        elif user.role == "doctor" and hasattr(user, "doctor"):
            queryset = Appointment.objects.filter(doctor=user.doctor)
        else:
            raise ProfileNotFound()

        # Filter the appointments based on the appointment_id
        if appointment_id:
            queryset = queryset.filter(appointment_id=appointment_id)

        return queryset

    def perform_create(self, serializer):
        """
        Create an appointment for the patient.
        """

        appointment_datetime, doctor = self.validate_appointment(serializer)

        serializer.save(
            patient=self.request.user.patient,
            doctor=doctor,
            start=appointment_datetime,
            end=appointment_datetime
            + datetime.timedelta(
                days=1
            ),  #! TODO: Remove timedelta after the feature (video call) is implemented
        )

    def perform_update(self, serializer):
        """
        Update the appointment for the patient.
        """

        appointment_datetime, doctor = self.validate_appointment(serializer)

        serializer.save(
            patient=self.request.user.patient,
            doctor=doctor,
            start=appointment_datetime,
            end=appointment_datetime
            + datetime.timedelta(
                days=1
            ),  #! TODO: Remove timedelta after the feature (video call) is implemented
        )

    def perform_destroy(self, instance):
        """
        Delete the appointment for the patient.
        """

        if not self.kwargs.get("appointment_id", None):
            raise URLKwargNotFound("Appointment ID")

        # Check if the appointment is in the past
        if instance.end < timezone.now() and instance.end:
            raise UnableToDestroyPastAppointment()
        else:
            instance.delete()

        return send_response("Appointment deleted successfully.", 200)

    def validate_appointment(self, serializer):
        """
        Validate appointment time.
        """

        appointment_start = self.request.data.get("start")
        doctor = DoctorProfile.objects.get(user=self.request.data.get("doctor"))

        appointment_start = datetime.datetime.fromisoformat(appointment_start)
        appointment_start = timezone.make_aware(appointment_start)

        # Check if the appointment is in the past
        if appointment_start < timezone.now():
            raise PastAppointment()

        day = appointment_start.strftime("%A").lower()
        time = appointment_start.strftime("%H:%M:%S")

        # Check if the doctor has set their availability
        if not doctor.availability_set.exists():
            raise DoctorAvailabilityNotFound()

        query = Q(day=day) & Q(start_time__lte=time) & Q(end_time__gte=time)

        # Check if the doctor is available on the selected date and time
        if not doctor.availability_set.filter(query).exists():
            raise DoctorNotAvailable()

        return appointment_start, doctor
