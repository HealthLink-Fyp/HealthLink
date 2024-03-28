# Local Imports
from patient.models import Appointment
from patient.serializers import AppointmentSerializer
from core.models import DoctorProfile
from core.authentication import JWTAuthentication

# Rest Framework Imports
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Django Imports
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.utils import timezone

# Python Imports
import datetime


class AppointmentView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    search_fields = ["doctor__full_name"]
    pagination_class = None

    def get_queryset(self):
        """
        Return the appointments of the user based on their role.
        """

        user = self.request.user

        if not user.role:
            self.error_response("You are not authorized to access appointments.")

        if user.role == "patient":
            queryset = Appointment.objects.filter(patient=user.patient)
        elif user.role == "doctor":
            queryset = Appointment.objects.filter(doctor=user.doctor)
        elif user.role == "admin":
            self.error_response(
                "Admins login through the admin panel."
            )  #!TODO: Add admin api endpoint

        return queryset

    def perform_create(self, serializer):
        """
        Create an appointment for the patient.
        """
        patient = self.request.user.patient

        if not patient:
            self.error_response("You are not authorized to create appointments.")

        doctor = get_object_or_404(DoctorProfile, user=self.request.data.get("doctor"))

        if not doctor:
            self.error_response("Doctor not found.")

        appointment_datetime_str = self.request.data.get("start")

        if not appointment_datetime_str:
            self.error_response("Appointment date and time is required.")

        try:
            appointment_datetime = timezone.make_aware(
                datetime.datetime.fromisoformat(appointment_datetime_str)
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

        serializer.save(
            patient=patient,
            doctor=doctor,
            start=appointment_datetime,
            end=appointment_datetime
            + datetime.timedelta(days=1),  #! TODO: Remove timedelta after resetdb
        )

        def error_response(self, message):
            return Response(
                {"error": message},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def perform_update(self, serializer):
        """
        Update the appointment for the patient.
        """
        patient = self.request.user.patient

        if not patient:
            self.error_response("You are not authorized to update appointments.")

        doctor = get_object_or_404(DoctorProfile, user=self.request.data.get("doctor"))

        if not doctor:
            self.error_response("Doctor not found.")

        appointment_datetime_str = self.request.data.get("start")

        if not appointment_datetime_str:
            self.error_response("Appointment date and time is required.")

        try:
            appointment_datetime = timezone.make_aware(
                datetime.datetime.fromisoformat(appointment_datetime_str)
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

        serializer.save(
            patient=patient,
            doctor=doctor,
            start=appointment_datetime,
            end=appointment_datetime
            + datetime.timedelta(days=1),  #! TODO: Remove timedelta after resetdb
        )

        def error_response(self, message):
            return Response(
                {"error": message},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def perform_destroy(self, instance):
        """
        Delete the appointment for the patient.
        """
        patient = self.request.user.patient

        if not patient:
            self.error_response("You are not authorized to delete appointments.")

        instance.delete()
