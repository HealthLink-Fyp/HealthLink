from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.authentication import JWTAuthentication

from healthlink.utils.exceptions import (
    NotFound,
    PatientNotAllowed,
    InvalidData,
    BadRequest,
)

from chat.models import Call
from chat.serializers import CallSerializer

from llm.chat_openai import send_transcription_to_chatbot


class CallView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        user = request.user

        if user.role == "patient" and hasattr(user, "patient"):
            call = Call.objects.filter(patient=user.patient).last()
            if call:
                return Response(
                    {
                        "peer_id": call.peer_id,
                        "call_id": call.call_id,
                        "doctor_id": call.doctor_id,
                    },
                    status=status.HTTP_200_OK,
                )
            raise NotFound("Call for patient")

        elif user.role == "doctor" and hasattr(user, "doctor"):
            call = Call.objects.filter(doctor=user.doctor).last()
            if call:
                return Response(
                    {
                        "call_id": call.call_id,
                        "patient_id": call.patient_id,
                    },
                    status=status.HTTP_200_OK,
                )
            raise NotFound("Call for doctor")

        serializer = CallSerializer(call, many=True)
        return Response(serializer.data)

    def post(self, request):
        peer_id = request.data.get("peer_id")

        if not peer_id:
            raise NotFound("Peer ID")

        serializer = CallSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CallTranscriptView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        call_id = request.data.get("call_id")
        patient_id = request.data.get("patient_id")
        transcription = request.data.get("transcription")

        if (
            not call_id
            or not patient_id
            or not transcription
            or len(transcription) == 0
        ):
            raise NotFound("call_id, patient_id, or transcription")

        if request.user.role == "patient" and hasattr(request.user, "patient"):
            raise PatientNotAllowed().default_detail + " send transcription"

        call = Call.objects.get(call_id=call_id)

        if not call or call.patient_id != patient_id:
            raise InvalidData("Call ID or Patient ID")

        response = send_transcription_to_chatbot(transcription)
        if "error" in response:
            raise BadRequest(response["error"])
        return Response(response, status=status.HTTP_200_OK)
