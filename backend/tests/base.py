from core.models import User
from rest_framework.test import APIClient, APITestCase


class BaseApiTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

class AuthenticatedApiTest(BaseApiTest):
    def setUp(self, role):
        super().setUp()
        self.user = User.objects.create_user(
            first_name="abc",
            last_name="xyz",
            email="abc@gmail.com",
            password="user@123",
            username="demo",
            role=role,
        )
        self.client.force_authenticate(user=self.user)

