from django.urls import reverse
from rest_framework import status

from patient.models import MedicineShop, MedicalTest
from .base import BaseApiTest

from .helpers import shop_data


class MedicineShopTest(BaseApiTest):
    def setUp(self):
        super().setUp()
        shop_data.add_medicines()

    def test_get_medicine_shop(self):
        url = reverse("medicine-shop")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("count"), MedicineShop.objects.count())

    def test_get_medicine_shop_detail(self):
        medicine = MedicineShop.objects.first()
        url = reverse(
            "medicine-shop-detail", kwargs={"medicine_id": medicine.medicine_id}
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get("medicine_id"), medicine.medicine_id)


class MedicalTestTest(BaseApiTest):
    def setUp(self):
        super().setUp()
        shop_data.add_medical_tests()

    def test_get_medical_test(self):
        url = reverse("medical-test")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("count"), MedicalTest.objects.count())

    def test_get_medical_test_detail(self):
        medical_test = MedicalTest.objects.first()
        url = reverse("medical-test-detail", kwargs={"test_id": medical_test.test_id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0].get("test_id"), medical_test.test_id)
