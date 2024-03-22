from core.models import User
from rest_framework.test import APIClient, APITestCase

from core.models import DoctorProfile, PatientProfile

from .variables import user_profile_data, doctor_profile_data, patient_profile_data


class BaseApiTest(APITestCase):
    def setUp(self):
        self.client = APIClient()


class AuthenticatedApiTest(BaseApiTest):
    def setUp(self, role):
        super().setUp()
        self.user = User.objects.create_user(role=role, **user_profile_data)
        self.client.force_authenticate(user=self.user)


class DoctorApiTest(AuthenticatedApiTest):
    def setUp(self):
        super().setUp(role="doctor")
        self.doctor = DoctorProfile.objects.create(
            user=self.user, **doctor_profile_data
        )


class PatientApiTest(AuthenticatedApiTest):
    def setUp(self):
        super().setUp(role="patient")
        self.patient = PatientProfile.objects.create(**patient_profile_data)
