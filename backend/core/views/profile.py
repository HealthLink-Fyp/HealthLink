# Rest Framework Imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Local Imports
from core.models import DoctorProfile, PatientProfile
from core.serializers import DoctorProfileSerializer, PatientProfileSerializer
from core.authentication import JWTAuthentication
from healthlink.utils.response_handler import send_response

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

        if not user:
            return send_response("User not found.", 404)

        if user.role == "doctor":
            profile = get_object_or_404(DoctorProfile, user=user)
            serializer = DoctorProfileSerializer(profile)

        elif user.role == "patient":
            profile = get_object_or_404(PatientProfile, user=user)
            serializer = PatientProfileSerializer(profile)
        else:
            return send_response("Not allowed.", 403)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create the user profile
        """
        user = request.user
        data = request.data.copy()
        data["user"] = user.id

        if user.role == "doctor":
            if DoctorProfile.objects.filter(user=user).exists():
                return send_response("Doctor profile already exists.", 403)

            serializer = DoctorProfileSerializer(data=data)

        elif user.role == "patient":
            if PatientProfile.objects.filter(user=user).exists():
                return send_response("Patient profile already exists.", 403)

            serializer = PatientProfileSerializer(data=data)

        else:
            return send_response("Not allowed.", 403)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request):
        """
        Update the user profile
        """
        user = request.user

        if user.role == "doctor":
            profile = get_object_or_404(DoctorProfile, user=user)
            serializer = DoctorProfileSerializer(profile, request.data, partial=True)
        elif user.role == "patient":
            profile = get_object_or_404(PatientProfile, user=user)
            serializer = PatientProfileSerializer(profile, request.data, partial=True)
        else:
            return send_response("Not allowed.", 403)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request):
        """
        Delete the user profile
        """
        user = request.user

        if user.role == "doctor":
            profile = DoctorProfile.objects.get(user=user)
        elif user.role == "patient":
            profile = PatientProfile.objects.get(user=user)
        else:
            return send_response("Not allowed.", 403)

        profile.delete()

        return send_response("Profile deleted successfully.", 200)
