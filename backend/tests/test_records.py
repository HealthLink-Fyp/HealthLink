from .base import PatientApiTest, DoctorApiTest
from django.urls import reverse
from rest_framework import status
from .variables import get_record_data


class MedicalRecordTests(DoctorApiTest, PatientApiTest):
    def setUp(self):
        super().setUp()
        self.create_doctor()
        self.create_patient()

    def create_medical_record(self):
        url = reverse("medical-record")
        record_data = get_record_data()
        record_data["doctor"] = self.doctor.user.id
        record_data["patient"] = self.patient.user.id
        self.response = self.client.post(url, data=record_data, format="multipart")

    def test_create_medical_record(self):
        self.create_medical_record()
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(self.response.data["doctor_note"], "Test doctor note")

    def test_get_medical_record(self):
        self.create_medical_record()
        url = reverse("medical-record")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["results"][0]["doctor_note"], "Test doctor note")

    def test_update_medical_record(self):
        self.create_medical_record()
        url = reverse("medical-record")
        record_id = self.response.data["record_id"]
        url = reverse("medical-record-detail", kwargs={"pk": record_id})
        data = {
            "doctor_note": "Updated doctor note",
            "llm_note": "Updated llm note",
        }
        response = self.client.patch(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["doctor_note"], "Updated doctor note")

    def test_delete_medical_record(self):
        self.create_medical_record()
        url = reverse("medical-record")
        record_id = self.response.data["record_id"]
        url = reverse("medical-record-detail", kwargs={"pk": record_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)
