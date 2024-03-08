from .base import AuthenticatedApiTest
from core.models import User
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
