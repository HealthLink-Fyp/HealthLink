from .base import AuthenticatedApiTest
from django.urls import reverse
from rest_framework import status


class ProfileTests(AuthenticatedApiTest):
    def setUp(self):
        super().setUp("patient")

    def test_no_profile(self):
        url = reverse("profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patient_profile(self):
        url = reverse("profile")
        data = {"age": 20, "sex": 0, "blood_group": "A+", "weight": 60, "height": 170}
        response = self.client.post(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_patient_profile_invalid_data(self):
        url = reverse("profile")
        response = self.client.post(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_doctor_profile(self):
        self.user.role = "doctor"
        self.user.save()
        url = reverse("profile")
        user_id = self.user.id
        print("\n\n\n", user_id, "\n\n\n")
        data = {
            "user_id": user_id,
            "specialization": "cardiologist",
            "qualification": "mbbs",
            "experience_years": 5,
            "city": "delhi",
            "available_timings": "10:00:00",
            "available_days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "consultation_fees": 500,
            "summary": "Dr. John Doe is a Cardiologist in Delhi with 5 years of experience.",
            "wait_time": 15,
            "recommendation_percent": 90,
            "patients_count": 100,
            "reviews_count": 50,
        }
        response = self.client.post(url, data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_doctor_profile_invalid_data(self):
        self.user.role = "doctor"
        self.user.save()
        url = reverse("profile")
        response = self.client.post(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_admin_profile(self):
        self.user.role = "admin"
        self.user.save()
        url = reverse("profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.post(url, data={}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
