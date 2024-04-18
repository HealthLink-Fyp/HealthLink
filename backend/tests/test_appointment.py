from .base import PatientApiTest, DoctorApiTest
from django.urls import reverse
from rest_framework import status
from core.serializers import DoctorProfileSerializer


class AppointmentTests(PatientApiTest, DoctorApiTest):
    def setUp(self):
        super().setUp()

        self.doctor = self.create_doctor_with_availabilities()

    def test_create_appointment(self):
        data = {
            "doctor": DoctorProfileSerializer(self.doctor).data.get("user"),
            "start": "2025-01-06T12:00:00",
        }

        response = self.client.post(reverse("appointment"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_appointment_invalid_date(self):
        data = {
            "doctor": DoctorProfileSerializer(self.doctor).data.get("user"),
            "start": "invalid_date",
        }

        response = self.client.post(reverse("appointment"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_doctor_not_available(self):
        data = {
            "doctor": DoctorProfileSerializer(self.doctor).data.get("user"),
            "start": "2025-01-01T12:00:00",
        }

        response = self.client.post(reverse("appointment"), data)
        self.assertEqual(response.data.get("code"), "doctor_not_available")
