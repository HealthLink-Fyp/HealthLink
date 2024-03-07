from core.models import DoctorProfile, PatientProfile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.serializers import DoctorProfileSerializer, PatientProfileSerializer

from django.core.exceptions import ObjectDoesNotExist

from core.authentication import JWTAuthentication

class ProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user

        try:
            if user.role == 'doctor':
                profile = DoctorProfile.objects.get(user=user)
                serializer = DoctorProfileSerializer(profile)
            elif user.role == 'patient':
                profile = PatientProfile.objects.get(user=user)
                serializer = PatientProfileSerializer(profile)
            else:
                return Response({"detail","Only doctor and patient allowed!"}, status=status.HTTP_403_FORBIDDEN)

            return Response(serializer.data, status=status.HTTP_200_OK)
            
        except ObjectDoesNotExist:
            return Response({"detail","Profile not found."}, status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        user = request.user
        payload = request.data
        payload['user'] = user.id

        if user.role == 'doctor':
            serializer = DoctorProfileSerializer(data=payload)
        elif user.role == 'patient':
            serializer = PatientProfileSerializer(data=payload)
        else:
            return Response({"detail": "Only doctor and patient allowed!"}, status=status.HTTP_403_FORBIDDEN)
            
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

