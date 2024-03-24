# Local Imports
from patient.models import Appointment
from patient.serializers import AppointmentSerializer

from core.models import DoctorProfile, Availability
from core.authentication import JWTAuthentication
# from core.serializers import DoctorProfileSerializer, AvailabilitySerializer

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ParseError
from rest_framework.response import Response


from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.utils import timezone

import datetime


class AppointmentView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    search_fields = ["doctor__full_name"]
    pagination_class = None

    def get_queryset(self):
        user = self.request.user

        if user.role == "patient":
            queryset = Appointment.objects.filter(patient=user.patient)
        elif user.role == "doctor":
            queryset = Appointment.objects.filter(doctor=user.doctor)
        else:
            queryset = None

        return queryset

    def perform_create(self, serializer):
        patient = self.request.user.patient
        doctor = get_object_or_404(DoctorProfile, user=self.request.data.get("doctor"))

        appointment_datetime_str = self.request.data.get("start")

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
