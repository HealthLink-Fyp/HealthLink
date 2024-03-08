from core.models import User
from django.urls import reverse
from rest_framework import status

from .base import BaseApiTest


class SignInEndpointTests(BaseApiTest):
    def setUp(self):
        super().setUp()
        user = User.objects.create(email="abc@gmail.com")
        user.set_password("user@123")
        user.save()

    def test_with_data(self):
        url = reverse("login")
        data = {"email": "abc@gmail.com", "password": "user@123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(
            list(response.data.keys()), ["access_token", "refresh_token"]
        )

    def test_missing_data(self):
        url = reverse("login")
        response = self.client.post(url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("missing", response.data[0])

    def test_validate_email(self):
        url = reverse("login")
        data = {"email": "abc@gmail", "password": "user@123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIn("Invalid email", response.data["message"])

    # def test_invalid_credentials(self):
    #     url = reverse("login")
    #     data_with_invalid_password = {"email": "abc@gmail.com", "password": "user123"}
    #     response = self.client.post(url, data_with_invalid_password, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertIn("Invalid credentials", response.data["message"])
    #     data_with_invalid_email = {"email": "ab@gmail.com", "password": "user@123"}
    #     response = self.client.post(url, data_with_invalid_email, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertIn("Invalid credentials", response.data["message"])

    # def test_not_logged_in(self):
    #     url = reverse("user")
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #     self.assertIn("Not authenticated", response.data["message"])
