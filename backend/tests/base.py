from core.models import User
from rest_framework.test import APIClient, APITestCase

from core.models import DoctorProfile, PatientProfile

from .variables import user_profile_data, doctor_profile_data, patient_profile_data


class BaseApiTest(APITestCase):
    def setUp(self):
        self.client = APIClient()


class AuthenticatedApiTest(BaseApiTest):
    def setUp(self, role=None):
        super().setUp()
        self.user = User.objects.create_user(role=role, **user_profile_data)
        self.client.force_authenticate(user=self.user)


class DoctorApiTest(AuthenticatedApiTest):
    def setUp(self, role=None):
        super().setUp(role="doctor")
        self.doctor_profile_data = doctor_profile_data.copy()
        self.doctor_profile_data["user"] = self.user

    def create_doctor(self):
        self.doctor_profile_data = self.doctor_profile_data.copy()
        self.doctor_profile_data.pop("availability_data")
        return DoctorProfile.objects.create(**self.doctor_profile_data)

    def create_doctor_with_availabilities(self):
        self.doctor = self.create_doctor()
        self.doctor_availability_data = {
            "doctor": self.doctor,
            "day": doctor_profile_data["availability_data"]["days"][0],
            "start_time": doctor_profile_data["availability_data"]["start"],
            "end_time": doctor_profile_data["availability_data"]["end"],
        }
        self.doctor.availability_set.create(**self.doctor_availability_data)
        return self.doctor


class PatientApiTest(AuthenticatedApiTest):
    def setUp(self):
        super().setUp(role="patient")
        self.patient_profile_data = patient_profile_data.copy()
        self.patient_profile_data["user"] = self.user
        self.patient = PatientProfile.objects.create(**self.patient_profile_data)
