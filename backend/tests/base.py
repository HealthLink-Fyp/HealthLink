from core.models import User
from rest_framework.test import APIClient, APITestCase

from core.models import DoctorProfile, PatientProfile

from .variables import (
    user_profile_data,
    doctor_profile_data,
    patient_profile_data,
    doctor_availability_data,
)


class BaseApiTest(APITestCase):
    def setUp(self):
        self.client = APIClient()


class AuthenticatedApiTest(BaseApiTest):
    def setUp(self):
        super().setUp()
        profile_data = user_profile_data.copy()
        profile_data["email"] = f"{self.role}@a.b"
        self.user = User.objects.create_user(role=self.role, **profile_data)
        self.client.force_authenticate(user=self.user)


class DoctorApiTest(AuthenticatedApiTest):
    def setUp(self):
        self.role = "doctor"
        self.profile_data = doctor_profile_data.copy()
        super().setUp()
        self.profile_data["user"] = self.user

    def create_doctor(self):
        self.availability_data = self.profile_data.pop("availability_data")
        self.doctor = DoctorProfile.objects.create(**self.profile_data)

    def create_doctor_with_availabilities(self):
        self.create_doctor()
        self.doctor.availability_set.create(**doctor_availability_data)


class PatientApiTest(AuthenticatedApiTest):
    def setUp(self):
        self.role = "patient"
        self.data = patient_profile_data.copy()
        super().setUp()
        self.data["user"] = self.user

    def create_patient(self):
        self.patient = PatientProfile.objects.create(**self.data)
