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


class MedicineShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineShop
        fields = "__all__"


class MedicalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTest
        fields = "__all__"


# const file = event.target.files[0];
# const reader = new FileReader();
# reader.onload = (event) => {
#   const arrayBuffer = event.target.result;
#   const uint8Array = new Uint8Array(arrayBuffer);
#   // Send the uint8Array to Django
# };
# reader.readAsArrayBuffer(file);


class EmotionSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        fields = ("image",)
        model = None

    def validate_image(self, value):
        return value

    def create(self, validated_data):
        return validated_data

    def update(self, instance, validated_data):
        return validated_data

    def save(self, **kwargs):
        return self.validated_data
