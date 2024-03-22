from .base import DoctorApiTest
from django.urls import reverse
from rest_framework import status
from core.serializers import DoctorProfileSerializer, DoctorAutoCompleteSerializer


class SearchTests(DoctorApiTest):
    def setUp(self):
        super().setUp()

    def test_autocomplete_doctor(self):
        self.url = reverse("autocomplete") + "?city=Demo"
        self.serializer_data = DoctorAutoCompleteSerializer(instance=self.doctor).data
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response.data = dict(response.data[0])
        self.assertDictEqual(response.data, self.serializer_data)

    def test_search_doctor(self):
        self.url = reverse("search") + "?city=Demo"
        self.serializer_data = DoctorProfileSerializer(instance=self.doctor).data
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response.data = dict(dict(response.data)["results"][0])
        self.assertDictContainsSubset(response.data, self.serializer_data)

    def test_doctor_detail(self):
        self.url = reverse("doctor-detail", kwargs={"pk": self.doctor.pk})
        self.serializer_data = DoctorProfileSerializer(instance=self.doctor).data
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.serializer_data)
