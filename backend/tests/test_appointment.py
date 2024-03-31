from .base import PatientApiTest, DoctorApiTest
from django.urls import reverse
from rest_framework import status
from core.serializers import DoctorProfileSerializer


class AppointmentTests(PatientApiTest, DoctorApiTest):
    def setUp(self):
        super().setUp()

        self.doctor = self.create_doctor()

    def test_create_appointment(self):
        data = {
            "doctor": DoctorProfileSerializer(self.doctor).data["id"],
            "start": "2021-01-01T12:00:00Z",
        }

        response = self.client.post(reverse("appointment-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_appointment_invalid_date(self):
        data = {
            "doctor": DoctorProfileSerializer(self.doctor).data["id"],
            "start": "invalid_date",
        }

        response = self.client.post(reverse("appointment-list"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_appointment_in_past(self):
        data = {
            "doctor": DoctorProfileSerializer(self.doctor).data["id"],
            "start": "2020-01-01T12:00:00Z",
        }

        response = self.client.post(reverse("appointment-list"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_get_appointment(self):
    #     response = self.client.get(
    #         reverse("appointment-detail", kwargs={"pk": self.appointment.id})
    #     )
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
