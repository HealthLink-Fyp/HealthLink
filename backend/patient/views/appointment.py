# Python Imports
import datetime

# Django Imports
from django.db.models import Q
from django.utils import timezone

# Rest Framework Imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .exceptions import DoctorNotAvailable

# Local Imports
from core.models import DoctorProfile
from patient.models import Appointment
from core.authentication import JWTAuthentication
from patient.serializers import AppointmentSerializer
from healthlink.utils.response_handler import send_response


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
            return send_response("Appointment not found.", 404)

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
            return send_response(error_message, 400)
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

    def validate_appointment(self, serializer):
        """
        Validate appointment time.
        """

        appointment_start = self.request.data.get("start")

        doctor = DoctorProfile.objects.get(user=self.request.data.get("doctor"))

        if not appointment_start:
            return send_response("Appointment date and time is required.", 400)

        try:
            appointment_datetime = timezone.make_aware(
                datetime.datetime.fromisoformat(appointment_start)
            )
        except Exception:
            return send_response("Invalid appointment date and time.", 400)

        if appointment_datetime < timezone.now():
            return send_response("Appointments cannot be in the past.", 400)

        day = appointment_datetime.strftime("%A").lower()
        time = appointment_datetime.strftime("%H:%M:%S")

        if not doctor.availability_set.exists():
            return send_response("Doctor has not set their availability.", 400)

        query = Q(day=day) & Q(start_time__lte=time) & Q(end_time__gte=time)

        if not doctor.availability_set.filter(query).exists():
            raise DoctorNotAvailable()

        return appointment_datetime, doctor
