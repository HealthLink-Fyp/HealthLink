from rest_framework.serializers import ModelSerializer
from healthlink.utils.exceptions import NotFound
from .models import Appointment, MedicalRecord, MedicineShop

import secrets


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


class MedicalRecordSerializer(ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = "__all__"

    def create(self, validated_data):
        """
        Create a MedicalRecord object.
        """

        prescription = validated_data.get("prescription")
        test_result = validated_data.get("test_result")

        if not prescription or not test_result:
            raise ValueError("Both prescription and test_result are required.")

        if (
            not len(prescription.name.split(".")) > 1
            or not len(test_result.name.split(".")) > 1
        ):
            raise ValueError(
                f"File name should have an extension. {prescription.name} {test_result.name}"
            )

        prescription.name = (
            secrets.token_urlsafe(16) + "." + prescription.name.split(".")[-1]
        )
        test_result.name = (
            secrets.token_urlsafe(16) + "." + test_result.name.split(".")[-1]
        )

        return super().create(validated_data)


class MedicineShopSerializer(ModelSerializer):
    class Meta:
        model = MedicineShop
        fields = "__all__"
