from .base import DoctorApiTest
from django.urls import reverse
from rest_framework import status
from core.serializers import DoctorProfileSerializer, DoctorAutoCompleteSerializer


class SearchTests(DoctorApiTest):
    def setUp(self):
        super().setUp()
        super().create_doctor()

    def test_autocomplete_doctor(self):
        self.url = reverse("autocomplete-doctors") + "?city=Demo"
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data[0]
        self.serializer_data = DoctorAutoCompleteSerializer(instance=self.doctor).data
        self.serializer_data["profile_photo_url"] = response_data.get(
            "profile_photo_url"
        )
        self.assertEqual(self.serializer_data, response_data)

    def test_search_doctor(self):
        self.url = reverse("search-doctors") + "?city=Demo"
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = response.data.get("results")[0]
        self.serializer_data = DoctorProfileSerializer(instance=self.doctor).data
        self.serializer_data["profile_photo_url"] = response_data.get(
            "profile_photo_url"
        )
        self.assertDictContainsSubset(response_data, self.serializer_data)

    def test_doctor_detail(self):
        self.url = reverse("doctor-detail", kwargs={"pk": self.doctor.pk})
        self.serializer_data = DoctorProfileSerializer(instance=self.doctor).data
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.serializer_data["profile_photo_url"] = response.data.get(
            "profile_photo_url"
        )
        self.assertEqual(self.serializer_data, response.data)
