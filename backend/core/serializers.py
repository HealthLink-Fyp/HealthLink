from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField

from .models import User, DoctorProfile, PatientProfile


class UserSerializer(ModelSerializer):
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
            "address",
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


class DoctorProfileSerializer(ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = [
            "user",
            "specialization",
            "qualification",
            "experience_years",
            "city",
            "available_timings",
            "available_days",
            "consultation_fees",
            "summary",
            "wait_time",
            "recommendation_percent",
            "patients_count",
            "reviews_count",
            "profile_photo_url",
        ]


class DoctorSearchBarSerializer(ModelSerializer):
    full_name = SerializerMethodField()

    class Meta:
        model = DoctorProfile
        fields = (
            "user",
            "full_name",
            "specialization",
            "city",
            "profile_photo_url",
        )

    def get_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"


class PatientProfileSerializer(ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = "__all__"
