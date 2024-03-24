# Local Imports
from patient.models import Appointment
from patient.serializers import AppointmentSerializer

from core.models import DoctorProfile, Availability
from core.authentication import JWTAuthentication
# from core.serializers import DoctorProfileSerializer, AvailabilitySerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

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
        # availability = get_object_or_404(Availability, doctor=doctor)

        appointment_datetime_str = self.request.data.get("start")

        appointment_datetime = datetime.datetime.fromisoformat(appointment_datetime_str)

        now_datetime = datetime.datetime.now()

        print(patient)
        print(doctor)
        print(appointment_datetime)
        print(now_datetime)

        return Response("Appointment booked!")
