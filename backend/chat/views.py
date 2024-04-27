from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.authentication import JWTAuthentication

import datetime
from chat.models import Call
from chat.serializers import CallSerializer

from ml.openai.chat import send_transcription_to_chatbot
from ml.emotion.predictions import EmotionPredictor
from patient.models import Appointment

from healthlink.utils.exceptions import (
    NotFound,
    PatientNotAllowed,
    InvalidData,
    BadRequest,
    AppointmentNotConfirmed,
    AppointmentNotPaid,
    FutureAppointment,
    MissedAppointment,
)

from rest_framework.parsers import MultiPartParser


class CallView(APIView):
    # authentication_classes = [JWTAuthentication]

    def get(self, request):
        """
        Get the call details based on the user role.
        """
        # user = request.user
        # call = self.validate_and_get_call(user)
        call = Call.objects.last()
        serializer = CallSerializer(call)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a call based on the user role.
        """
        # user = request.user
        # peer_id = request.data.get("peer_id")

        # # Validate the peer ID
        # if not peer_id or not isinstance(peer_id, str):
        #     raise NotFound("Peer ID")

        # # Patient cannot create a call
        # if user.role == "patient" and hasattr(user, "patient"):
        #     raise PatientNotAllowed("Create call")

        # _ = self.validate_and_get_call(user)

        serializer = CallSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def validate_and_get_call(self, user):
        """
        Validate the call based on the user role and appointment.
        """
        appointment = self.get_latest_appointment(user)
        self.validate_appointment(appointment)
        call = self.get_latest_call(user)
        self.validate_call(call, appointment, user)
        return call

    def get_latest_appointment(self, user):
        if user.role == "patient" and hasattr(user, "patient"):
            return Appointment.objects.filter(patient=user.patient).last()
        elif user.role == "doctor" and hasattr(user, "doctor"):
            return Appointment.objects.filter(doctor=user.doctor).last()

    def validate_appointment(self, appointment):
        if not appointment:
            raise NotFound("Appointment")
        if appointment.appointment_status != "confirmed":
            raise AppointmentNotConfirmed()
        if appointment.payment_status != "paid":
            raise AppointmentNotPaid()
        if appointment.start + datetime.timedelta(minutes=5) > datetime.datetime.now():
            raise MissedAppointment()
        if appointment.start > datetime.datetime.now():
            raise FutureAppointment()

    def get_latest_call(self, user):
        if user.role == "patient" and hasattr(user, "patient"):
            return Call.objects.filter(patient=user.patient).last()
        elif user.role == "doctor" and hasattr(user, "doctor"):
            return Call.objects.filter(doctor=user.doctor).last()

    def validate_call(self, call, appointment, user):
        if not call:
            raise NotFound("Call")
        if user.role == "patient" and call.doctor != appointment.doctor:
            raise NotFound("Call for patient")
        elif user.role == "doctor" and call.patient != appointment.patient:
            raise NotFound("Call for doctor")


class CallTranscriptView(APIView):
    authentication_classes = [JWTAuthentication]

    def validate_data(self, data, data_type, name):
        """
        Validate the data based on the data type.
        """
        if not data or not isinstance(data, data_type):
            raise InvalidData(name)

    def post(self, request):
        """
        Send the transcription to the chatbot.
        """
        call_id = request.data.get("call_id")
        patient_id = request.data.get("patient_id")
        transcription = request.data.get("transcription")

        # Validate the data
        self.validate_data(call_id, str, "Call ID")
        self.validate_data(patient_id, str, "Patient ID")
        self.validate_data(transcription, str, "Transcription")

        # Patient cannot send transcription
        if request.user.role == "patient" and hasattr(request.user, "patient"):
            raise PatientNotAllowed("Send transcription")

        # Check if the call exists
        try:
            call = Call.objects.get(call_id=call_id)
        except Call.DoesNotExist:
            raise NotFound("Call")

        # Check if the call ID and patient ID match
        if not call or call.patient_id != patient_id:
            raise InvalidData("Call ID or Patient ID")

        # Check if the transcription is empty
        if call.patient_id != patient_id:
            raise InvalidData("Provided Patient ID does not match or")

        response = send_transcription_to_chatbot(transcription)

        # Check if the response from the chatbot is an error
        if "error" in response:
            raise BadRequest(response["error"])

        return Response(response, status=status.HTTP_200_OK)


class CallEmotionView(APIView):
    parser_classes = (MultiPartParser,)
    parser_classes[0].media_type = "multipart/form-data"
    predictor = EmotionPredictor()

    def post(self, request, *args, **kwargs):
        """
        Receive the image from the client, and send it to the emotion prediction model.
        """
        if "file" not in request.data:
            raise BadRequest("Image file not found in the request")

        image_file = request.data["file"]

        if not image_file:
            raise InvalidData("Image file is empty")

        try:
            emotion = self.predictor.predict(image_file.read())
            return Response({"emotion": emotion}, status=status.HTTP_200_OK)
        except Exception as e:
            raise BadRequest(str(e))
