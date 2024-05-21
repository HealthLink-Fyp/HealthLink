from rest_framework import serializers
from .models import Appointment, MedicalRecord, MedicineShop, MedicalTest


class AppointmentSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="doctor.full_name", read_only=True)

    class Meta:
        model = Appointment
        fields = "__all__"


class MedicalRecordSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="doctor.full_name", read_only=True)

    class Meta:
        model = MedicalRecord
        fields = [
            "record_id",
            "doctor_name",
            "doctor_notes",
            "past_records",
            "created",
        ]
        read_only_fields = ["patient", "doctor"]


class MedicineShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineShop
        fields = "__all__"


class MedicalTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalTest
        fields = "__all__"
