from rest_framework import serializers
from .models import Appointment, MedicalRecord, MedicineShop, MedicalTest

import secrets


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = "__all__"

    def create(self, validated_data):
        """
        Create a MedicalRecord object.
        """

        prescription = validated_data.get("prescription")

        if not isinstance(prescription, dict):
            raise ValueError("Prescription should be a dictionary.")

        if not prescription.get("medicines") or not prescription.get("tests"):
            raise ValueError("Prescription should have medicines and tests")

        past_records = validated_data.get("past_records")

        if past_records:
            if not len(past_records.name.split(".")) > 1:
                raise ValueError(
                    f"File name should have an extension. {past_records.name}"
                )

            past_records.name = (
                secrets.token_urlsafe(16) + "." + past_records.name.split(".")[-1]
            )

        return super().create(validated_data)


class MedicineShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineShop
        fields = "__all__"


class MedicalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTest
        fields = "__all__"
