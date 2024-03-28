from core.models import User
from django.urls import reverse
from rest_framework import status

from .base import BaseApiTest, AuthenticatedApiTest


class SignInEndpointTests(BaseApiTest):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create(email="abc@gmail.com")
        self.user.set_password("user@123")
        self.user.save()

    def test_with_data(self):
        url = reverse("login")
        data = {"email": "abc@gmail.com", "password": "user@123"}
        test_response_list = ["access_token", "refresh_token"]
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertListEqual(list(response.data.keys()), test_response_list)

    def test_without_data(self):
        url = reverse("login")
        response = self.client.post(url, {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_email(self):
        url = reverse("login")
        data = {"email": "abcgmail.com", "password": "user@123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_password(self):
        url = reverse("login")
        data_with_invalid_password = {"email": "abc@gmail.com", "password": "user123"}
        response = self.client.post(url, data_with_invalid_password, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_not_logged_in(self):
        url = reverse("user")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_as_admin(self):
        self.user.role = "admin"
        self.user.save()
        url = reverse("user")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class SignInEndpointAuthenticatedTests(AuthenticatedApiTest):
    def setUp(self):
        super().setUp("patient")

    def test_logged_in(self):
        url = reverse("user")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_as_doctor(self):
        self.user.role = "doctor"
        self.user.save()
        url = reverse("user")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_as_patient(self):
        self.user.role = "patient"
        self.user.save()
        url = reverse("user")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
