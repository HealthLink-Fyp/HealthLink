from django.db import transaction
from rest_framework import serializers
from .models import User, DoctorProfile, PatientProfile, Availability

from healthlink.utils.response_handler import send_response


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
        data = super().to_representation(instance)
        data["availability_data"] = self.get_availability_data(instance)
        return data

    def validate_availability_data(self, availability_data):
        if not isinstance(availability_data, dict):
            return send_response("availability_data must be a dictionary", 400)

        try:
            days = availability_data["days"]
            start_time = availability_data["start"]
            end_time = availability_data["end"]
        except KeyError:
            return send_response(
                "days, start, and end are required in availability_data", 400
            )

        import datetime

        start_time = datetime.datetime.strptime(start_time, "%H:%M")
        end_time = datetime.datetime.strptime(end_time, "%H:%M")

        if start_time >= end_time:
            return send_response("start time must be before end time", 400)

        if not isinstance(days, list) or len(days) == 0:
            return send_response("days must be a list of days", 400)

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
                "start_time": availability_data.get("start"),
                "end_time": availability_data.get("end"),
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
