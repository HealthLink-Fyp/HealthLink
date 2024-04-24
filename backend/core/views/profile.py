# Rest Framework Imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Local Imports
from core.models import DoctorProfile, PatientProfile
from core.serializers import DoctorProfileSerializer, PatientProfileSerializer
from core.authentication import JWTAuthentication
from healthlink.utils.exceptions import (
    ProfileNotFound,
    NotFound,
    AlreadyExists,
    AdminNotAllowed,
)

# Django Imports
from django.shortcuts import get_object_or_404


class ProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Get the user profile
        """
        user = request.user

        # Check if user exists
        if not user:
            raise NotFound("User")

        # Check if user has a profile
        if user.role == "doctor" and hasattr(user, "doctor"):
            profile = get_object_or_404(DoctorProfile, user=user)
            serializer = DoctorProfileSerializer(profile)

        elif user.role == "patient" and hasattr(user, "patient"):
            profile = get_object_or_404(PatientProfile, user=user)
            serializer = PatientProfileSerializer(profile)
        else:
            raise ProfileNotFound()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create the user profile
        """
        user = request.user

        # Check if user exists
        if not user:
            raise NotFound("User")

        data = request.data.copy()
        data["user"] = user.id

        # Check if user already has a profile
        if user.role == "doctor":
            if DoctorProfile.objects.filter(user=user).exists():
                raise AlreadyExists("Doctor profile")
            serializer = DoctorProfileSerializer(data=data)
        elif user.role == "patient":
            if PatientProfile.objects.filter(user=user).exists():
                raise AlreadyExists("Patient profile")
            serializer = PatientProfileSerializer(data=data)
        else:
            raise AdminNotAllowed()

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        """
        Update the user profile
        """
        user = request.user

        # Check if user has a profile
        if user.role == "doctor" and hasattr(user, "doctor"):
            profile = get_object_or_404(DoctorProfile, user=user)
            serializer = DoctorProfileSerializer(profile, request.data, partial=True)
        elif user.role == "patient" and hasattr(user, "patient"):
            profile = get_object_or_404(PatientProfile, user=user)
            serializer = PatientProfileSerializer(profile, request.data, partial=True)
        else:
            raise ProfileNotFound()

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        """
        Delete the user profile
        """
        user = request.user

        # Check if user has a profile
        if user.role == "doctor" and hasattr(user, "doctor"):
            profile = DoctorProfile.objects.get(user=user)
        elif user.role == "patient" and hasattr(user, "patient"):
            profile = PatientProfile.objects.get(user=user)
        else:
            raise ProfileNotFound()

        profile.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
