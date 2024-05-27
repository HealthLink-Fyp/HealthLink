from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Local Imports
from chat.models import Call, LLMResponse
from core.authentication import JWTAuthentication
from ml.openai.chat import send_transcription_to_chatbot

from healthlink.utils.exceptions import InvalidData, NotFound, BadRequest

# Django Imports
from django.core.cache import cache


class CallTranscriptView(APIView):
    authentication_classes = [JWTAuthentication]

    def transcript_handler(self, user, role):
        """
        Handle the transcription for the user.
        """
        if hasattr(user, role):
            person = getattr(user, role)
            call = Call.objects.filter(**{role: person}).last()
            # Check if the call exists
            if not call:
                raise NotFound("Call")
            # Check if the active call is for the user
            if getattr(call, role) != person:
                raise NotFound("Active Call for user")
            return call

        raise NotFound("User Role")

    def post(self, request):
        """
        Send the transcription to the chatbot.
        """

        user = request.user
        if not user:
            raise NotFound("User")

        role = user.role
        call = self.transcript_handler(user=user, role=role)

        transcription = request.data.get("transcription")
        if not transcription or not isinstance(transcription, str):
            raise InvalidData("Transcription")

        self.add_transcription_to_cache(transcription, role)

        transcriptions = self.get_transcriptions_from_cache()

        if len(transcriptions) >= 2 and role != "doctor":
            transcriptions.append(transcriptions.pop(1))
            cache.set("transcription", transcriptions, timeout=1000)

        if len(transcriptions) >= 1 and role == "doctor":
            return self.send_transcriptions_to_chatbot(call)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_transcriptions_from_cache(self):
        return cache.get("transcription", [])

    def add_transcription_to_cache(self, transcription, role):
        transcriptions = self.get_transcriptions_from_cache()
        transcriptions.append((transcription, role))
        cache.set("transcription", transcriptions, timeout=1000)

    def send_transcriptions_to_chatbot(self, call):
        transcriptions = self.get_transcriptions_from_cache()
        transcription_text = " ".join(
            [transcript_role_pair[0] for transcript_role_pair in transcriptions]
        )
        response = send_transcription_to_chatbot(transcription_text)

        if "error" in response:
            raise BadRequest(response["error"])

        response_text = self.json_to_paragraph(response)

        LLMResponse.objects.create(
            call=call,
            transcription=transcription_text,
            response=response,
            response_text=response_text,
        )
        cache.delete("transcription")

        return Response(response, status=status.HTTP_200_OK)

    def json_to_paragraph(self, data):
        """
        Convert the JSON data to a paragraph.
        """
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
