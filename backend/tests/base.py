from rest_framework.test import APIClient, APITestCase


class BaseApiTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
