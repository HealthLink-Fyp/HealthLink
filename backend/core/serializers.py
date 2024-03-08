from rest_framework.serializers import ModelSerializer

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
        fields = "__all__"


class PatientProfileSerializer(ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = "__all__"
