from django.urls import reverse
from rest_framework import status

# Other imports
# from backend.core.models import User
from backend.apps.core.models import User

from .base import BaseApiTest


class AccountTests(BaseApiTest):
    def test_create_account(self):
        url = reverse("register")
        data = {
            "first_name": "Faisal",
            "last_name": "Fida",
            "username": "faisal",
            "email": "faisal@gmail.com",
            "password": "ubiquitous",
            "password_confirm": "ubiquitous",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, "faisal@gmail.com")
