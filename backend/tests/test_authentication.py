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

    def test_without_data(self):
        url = reverse("login")
        response = self.client.post(url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_email(self):
        url = reverse("login")
        data = {"email": "useremail.com", "password": "user@123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {"error", "Please provide a valid email address"}
        )

    def test_password_validity(self):
        url = reverse("login")
        data = {"email": "abc@gmail.com", "password": "user123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            response.data,
            {
                "error": "Sorry, we could not find a user with the provided credentials. Please try again.",
            },
        )

    def test_user_exist(self):
        url = reverse("login")
        data = {"email": "xyz@gmail.com", "password": "user@123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(
            response.data,
            {
                "error": "Sorry, we could not find a user with the provided credentials. Please try again."
            },
        )
