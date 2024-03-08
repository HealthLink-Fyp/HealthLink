from core.models import DoctorProfile, PatientProfile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from core.serializers import DoctorProfileSerializer, PatientProfileSerializer

from core.authentication import JWTAuthentication

from .exceptions import missing_data_exception, admin_not_allowed_exception, user_not_found_exception

class ProfileView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        user_not_found_exception(user)

        if user.role == 'doctor':
            profile = DoctorProfile.objects.get(user=user)
            serializer = DoctorProfileSerializer(profile)
        elif user.role == 'patient':
            profile = PatientProfile.objects.get(user=user)
            serializer = PatientProfileSerializer(profile)
        else:
            admin_not_allowed_exception(user)

        return Response(serializer.data, status=status.HTTP_200_OK)
            


    def post(self, request):
        user = request.user
        payload = request.data
        payload['user'] = user.id

        missing_data_exception(payload.get('age', False), payload.get('first_name'))

        if user.role == 'doctor':
            serializer = DoctorProfileSerializer(data=payload)
        elif user.role == 'patient':
            serializer = PatientProfileSerializer(data=payload)
        else:
            admin_not_allowed_exception(user)
            
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

