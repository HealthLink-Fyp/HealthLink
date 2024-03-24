from django.db import transaction
from rest_framework import serializers
from .models import User, DoctorProfile, PatientProfile, Availability


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "role",
            "phone_number",
            "city",
            "password",
        )

        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        email = validated_data.get("email")
        email = email.lower().strip()
        validated_data["email"] = email
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = "__all__"


class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = (
            "user",
            "full_name",
            "city",
            "specialization",
            "qualification",
            "experience_years",
            "consultation_fees",
            "summary",
            "wait_time",
            "recommendation_percent",
            "patients_count",
            "reviews_count",
            "profile_photo_url",
            "created",
        )

    def get_availability_data(self, obj):
        data = {}
        availability = obj.availability_set.all()

        # check if availability exists
        if not availability.exists():
            return None

        data["days"] = [day.day for day in availability if day]
        data["start"] = availability[0].start_time if len(availability) > 0 else None
        data["end"] = availability[0].end_time if len(availability) > 0 else None

        return data

    @transaction.atomic
    def create(self, validated_data):
        availability_data = self.initial_data.get("availability_data")

        # check if availability_data is provided
        if availability_data is None:
            raise serializers.ValidationError("availability_data is required")

        # check if availability_data is a dictionary
        if not isinstance(availability_data, dict):
            raise serializers.ValidationError("availability_data must be a dictionary")

        days = availability_data.get("days")
        start_time = availability_data.get("start")
        end_time = availability_data.get("end")

        # check if days, start, and end are provided
        if (
            not days
            or not isinstance(days, list)
            or len(days) == 0
            or not start_time
            or not end_time
        ):
            raise serializers.ValidationError(
                "days, start, and end are required in availability_data"
            )

        doctor = DoctorProfile.objects.create(**validated_data)

        serializer_data = [
            {
                "doctor": doctor,
                "day": day,
                "start_time": availability_data.get("start"),
                "end_time": availability_data.get("end"),
            }
            for day in availability_data["days"]
        ]

        serializer = AvailabilitySerializer(data=serializer_data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return doctor


class DoctorAutoCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = (
            "user",
            "full_name",
            "city",
            "specialization",
            "profile_photo_url",
        )


class DoctorSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = (
            "user",
            "full_name",
            "city",
            "specialization",
            "profile_photo_url",
            "patients_count",
            "reviews_count",
            "recommendation_percent",
            "consultation_fees",
            "wait_time",
            "experience_years",
            "available_days",
        )


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = "__all__"
