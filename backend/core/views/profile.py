from core.models import DoctorProfile, PatientProfile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializers import DoctorProfileSerializer, PatientProfileSerializer


class DoctorProfileView(APIView):
    def get(self, request):
        profile = DoctorProfile.objects.filter(pk=request.user.pk)

        if profile.exists():
            serializer = PatientProfileSerializer(profile.first())
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Doctor Profile not found."}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = DoctorProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class PatientProfileView(APIView):
    def get(self, request):
        profile = PatientProfile.objects.filter(pk=request.user.pk)
        if profile.exists():
            serializer = PatientProfileSerializer(profile.first())
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "Patient Profile not found."}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = PatientProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    