from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

# Local Imports
from patient.models import Appointment
from chat.models import Call, LLMResponse, Chat
from chat.serializers import CallSerializer, ChatSerializer
from core.authentication import JWTAuthentication
from ml.emotion.predictions_v2 import EmotionPredictor
from ml.openai.chat import (
    send_transcription_to_chatbot,
    send_transcription_to_chatbot_v2,
)
from healthlink.utils.exceptions import (
    NotFound,
    PatientNotAllowed,
    InvalidData,
    BadRequest,
    # AppointmentNotConfirmed,
    # AppointmentNotPaid,
    # FutureAppointment,
    # MissedAppointment,
)


# Django Imports
from django.core.cache import cache


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
                raise InvalidData(f"Doctor {doctor} or Patient {patient}")
            chat = Chat.objects.filter(patient=patient, doctor=doctor)
        elif user.role == "doctor" and hasattr(user, "doctor"):
            doctor = user.doctor
            patient = request.data.get("patient")
            if (not doctor) or (not patient):
                raise InvalidData(f"Doctor {doctor} or Patient {patient}")
            chat = Chat.objects.filter(patient=patient, doctor=doctor)

        if not chat:
            raise NotFound("Chat")

        serializer = ChatSerializer(chat, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CallView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        """
        Get the call details based on the user role.
        """
        user = request.user
        # call = self.validate_and_get_call(user)

        appointment = self.get_latest_appointment(user)
        self.validate_appointment(appointment)
        call = self.get_latest_call(user)
        self.validate_call(call, appointment, user)

        # call = Call.objects.last()
        serializer = CallSerializer(call)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create a call based on the user role.
        """
        user = request.user
        peer_id = request.data.get("peer_id")

        # Validate the peer ID
        if not peer_id or not isinstance(peer_id, str):
            raise NotFound("Peer ID")

        # Patient cannot create a call
        if user.role == "patient" and hasattr(user, "patient"):
            raise PatientNotAllowed()
 
        appointment = self.get_latest_appointment(user)
        self.validate_appointment(appointment)

        serializer = CallSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def validate_and_get_call(self, user):
    #     """
    #     Validate the call based on the user role and appointment.
    #     """
    #     appointment = self.get_latest_appointment(user)
    #     self.validate_appointment(appointment)
    #     call = self.get_latest_call(user)
    #     self.validate_call(call, appointment, user)
    #     return call

    def get_latest_appointment(self, user):
        if user.role == "patient" and hasattr(user, "patient"):
            return Appointment.objects.filter(patient=user.patient).last()
        elif user.role == "doctor" and hasattr(user, "doctor"):
            return Appointment.objects.filter(doctor=user.doctor).last()

    def validate_appointment(self, appointment):
        if not appointment:
            raise NotFound("Appointment")
        # if appointment.appointment_status != "confirmed":
        #     raise AppointmentNotConfirmed()
        # if appointment.payment_status != "paid":
        #     raise AppointmentNotPaid()
        # if appointment.start + datetime.timedelta(minutes=5) > datetime.datetime.now():
        #     raise MissedAppointment()
        # if appointment.start > datetime.datetime.now():
        #     raise FutureAppointment()

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

    def post(self, request):
        """
        Send the transcription to the chatbot.
        """

        user = request.user

        # Patient cannot send transcription
        if user.role == "patient" and hasattr(user, "patient"):
            patient = user.patient
            call = Call.objects.filter(patient=patient).last()
            role = "patient"
            # Check if the call exists
            if not call:
                raise NotFound("Call")
            # Check if the active call is for the patient
            if call.patient != patient:
                raise NotFound("Active Call for patient")
            doctor = None

        elif user.role == "doctor" and hasattr(user, "doctor"):
            doctor = user.doctor
            call = Call.objects.filter(doctor=doctor).last()
            role = "doctor"
            # Check if the call exists
            if not call:
                raise NotFound("Call")
            # Check if the active call is for the doctor
            if call.doctor != doctor:
                raise NotFound("Active Call for doctor")
            patient = None

        # Check if the doctor exists
        if (not doctor) and (not patient):
            raise NotFound("Doctor or Patient")

        transcription = request.data.get("transcription")

        # Check if the transcription is empty
        if not transcription or not isinstance(transcription, str):
            raise InvalidData("Transcription")

        if cache.get("transcription") is not None:
            transcriptions = cache.get("transcription")
            transcriptions.append((transcription, role))
            cache.set("transcription", transcriptions, timeout=1000)

            if len(transcriptions) > 2 and role != "doctor":
                """
                Don't send the transcriptions to the chatbot.
                As the patient is not the last one to send the transcription.
                """
                transcriptions.append(transcriptions.pop(1))
                cache.set("transcription", transcriptions, timeout=1000)

            if len(transcriptions) >= 2 and role == "doctor":
                """
                Send the transcriptions to the chatbot.
                As the doctor is the last one to send the transcription.
                """
                transcription = " ".join([t[0] for t in transcriptions])
                response = send_transcription_to_chatbot(transcription)

                # Check if the response from the chatbot is an error
                if "error" in response:
                    raise BadRequest(response["error"])

                LLMResponse.objects.create(
                    call=call, transcription=transcription, response=response
                )

                cache.delete("transcription")

                return Response(response, status=status.HTTP_200_OK)
        else:
            transcriptions = []
            transcriptions.append((transcription, role))
            cache.set("transcription", transcriptions, timeout=1000)

        return Response(status=status.HTTP_204_NO_CONTENT)


class DashboardReportView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        """
        Send the medical report to the chatbot.
        """

        patient = request.user.patient

        llm_responses = LLMResponse.objects.filter(call__patient=patient)

        if not llm_responses:
            raise NotFound("LLM Responses")

        llm_data = ""

        for llm_response in llm_responses:
            if isinstance(llm_response.response, dict):
                llm_data += json_to_paragraph(llm_response.response)

        response = send_transcription_to_chatbot_v2(llm_data)

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


def json_to_paragraph(data):
    key_points = data.get("key_points", [])
    likely_diagnoses = data.get("likely_diagnoses", [])
    followup_questions = data.get("followup_questions", [])

    paragraph = "Common symptoms include "
    if key_points:
        paragraph += ", ".join(key_points)

    if likely_diagnoses:
        paragraph += ". Based on your symptoms, you may have "
        diagnoses_text = []
        for diagnosis, chance in likely_diagnoses:
            diagnoses_text.append(f"{diagnosis} ({chance} chance)")
        paragraph += ", ".join(diagnoses_text)

    if followup_questions:
        paragraph += ". To further assess your condition, I would like to ask you some follow-up questions: "
        paragraph += " ".join(followup_questions)

    return paragraph
