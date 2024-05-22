from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Local Imports
from chat.models import Chat
from chat.serializers import ChatSerializer
from core.authentication import JWTAuthentication

from healthlink.utils.exceptions import InvalidData


class ChatView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        """
        Get the chat messages history based on the user role.
        """
        user = request.user

        if user.role == "patient" and hasattr(user, "patient"):
            patient = user.patient
            doctor = request.data.get("doctor")
            if (not doctor) or (not patient):
                raise InvalidData("Doctor or Patient")
            chat = Chat.objects.filter(patient=patient, doctor=doctor)
        elif user.role == "doctor" and hasattr(user, "doctor"):
            doctor = user.doctor
            patient = request.data.get("patient")
            if (not doctor) or (not patient):
                raise InvalidData("Doctor or Patient")
            chat = Chat.objects.filter(patient=patient, doctor=doctor)

        if not chat:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = ChatSerializer(chat, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
