from django.db import transaction
from rest_framework import serializers
from .models import User, DoctorProfile, PatientProfile, Availability

from healthlink.utils.exceptions import (
    InvalidAvailabilityData,
    InvalidAvailabilityTime,
    InvalidAvailabilityDay,
)


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


class AvailabilityDataMixin:
    availability_data = serializers.SerializerMethodField()

    def get_availability_data(self, obj):
        data = {}
        availability = obj.availability_set.all()

        # check if availability exists
        if len(availability) > 0:
            data["days"] = [day.day for day in availability if day]
            data["start"] = availability[0].start_time
            data["end"] = availability[0].end_time

        return data if data else None


class DoctorProfileSerializer(AvailabilityDataMixin, serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = (
            "user",
            "full_name",
            "sex",
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

    def to_representation(self, instance):
        data = super().to_representation(instance)  # Call the parent method
        data["availability_data"] = self.get_availability_data(instance)
        return data

    def validate_availability_data(self, availability_data):
        # Check if availability data is a dictionary
        if not isinstance(availability_data, dict):
            raise InvalidAvailabilityData()

        days = availability_data.get("days", None)
        start_time = availability_data.get("start", None)
        end_time = availability_data.get("end", None)

        # Check if days, start_time and end_time are provided
        if not days or not start_time or not end_time:
            raise InvalidAvailabilityData()

        from datetime import datetime

        start_time = datetime.strptime(start_time, "%H:%M").time()
        end_time = datetime.strptime(end_time, "%H:%M").time()

        if start_time >= end_time:
            raise InvalidAvailabilityTime()

        if not isinstance(days, list) or len(days) == 0:
            raise InvalidAvailabilityDay()

        return days, start_time, end_time

    @transaction.atomic
    def create(self, validated_data):
        availability_data = self.initial_data.get("availability_data")
        days, start_time, end_time = self.validate_availability_data(availability_data)
        doctor = DoctorProfile.objects.create(**validated_data)

        serializer_data = [
            {
                "doctor": doctor,
                "day": day,
                "start_time": start_time,
                "end_time": end_time,
            }
            for day in days
        ]

        serializer = AvailabilitySerializer(data=serializer_data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return doctor

    @transaction.atomic
    def update(self, instance, validated_data):
        availability_data = self.initial_data.get("availability_data")
        days, start_time, end_time = self.validate_availability_data(availability_data)

        for day in days:
            availability = instance.availability_set.filter(day=day).first()
            if availability:
                availability.start_time = start_time
                availability.end_time = end_time
                availability.save()
            else:
                Availability.objects.create(
                    doctor=instance, day=day, start_time=start_time, end_time=end_time
                )

        return super().update(instance, validated_data)


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


class DoctorSearchSerializer(AvailabilityDataMixin, serializers.ModelSerializer):
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
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["availability_data"] = self.get_availability_data(instance)
        return data


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = "__all__"
