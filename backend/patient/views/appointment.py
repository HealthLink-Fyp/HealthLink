# Python Imports
import datetime

# Django Imports
from django.db.models import Q
from django.utils import timezone

# Rest Framework Imports
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Local Imports
from core.models import DoctorProfile
from patient.models import Appointment
from core.authentication import JWTAuthentication
from patient.serializers import AppointmentSerializer


class AppointmentView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = None
    lookup_field = "appointment_id"

    def get(self, request, *args, **kwargs):
        if "appointment_id" in kwargs:
            self.object = self.get_object()
            return self.retrieve(request, *args, **kwargs)
        else:
            return super().get(request, *args, **kwargs)

    def get_object(self):
        """
        Return the appointment object based on the user's role.
        """

        pk = self.kwargs.get("appointment_id")
        user = self.request.user

        if user.role == "patient":
            queryset = Appointment.objects.filter(
                patient=user.patient, appointment_id=pk
            )
        elif user.role == "doctor":
            queryset = Appointment.objects.filter(doctor=user.doctor, appointment_id=pk)

        if not queryset:
            self.error_response("Appointment not found.")

        return queryset.first()

    def get_queryset(self):
        """
        Return the appointments of the user based on their role.
        """

        user = self.request.user

        if user.role == "patient":
            queryset = Appointment.objects.filter(patient=user.patient)
        elif user.role == "doctor":
            queryset = Appointment.objects.filter(doctor=user.doctor)
        else:
            queryset = Appointment.objects.none()

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
        error_message = self.is_appointment_active(instance)

        if error_message:
            self.error_response(error_message)
        else:
            instance.delete()

        return None

    def is_appointment_active(self, instance):
        now = timezone.now()
        if instance.end and instance.end < now:
            return "Cannot delete an appointment that has already ended."
        elif instance.start < now:
            return "Cannot delete an appointment that has already started."
        return None

    def error_response(self, message):
        """
        Raise an error response.
        """
        raise APIException({"error": message})

    def validate_appointment(self, serializer):
        """
        Validate appointment time.
        """

        appointment_start = self.request.data.get("start")

        doctor = DoctorProfile.objects.get(user=self.request.data.get("doctor"))

        if not appointment_start:
            self.error_response("Appointment date and time is required.")

        try:
            appointment_datetime = timezone.make_aware(
                datetime.datetime.fromisoformat(appointment_start)
            )
        except Exception:
            self.error_response("Invalid date and time format.")

        if appointment_datetime < timezone.now():
            self.error_response("Appointment date and time cannot be in the past.")

        day = appointment_datetime.strftime("%A").lower()
        time = appointment_datetime.strftime("%H:%M:%S")

        if not doctor.availability_set.exists():
            self.error_response("Doctor has not set their availability.")

        query = Q(day=day) & Q(start_time__lte=time) & Q(end_time__gte=time)

        if not doctor.availability_set.filter(query).exists():
            self.error_response(
                "Doctor is not available at the selected date and time."
            )

        return appointment_datetime, doctor