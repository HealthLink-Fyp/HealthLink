# Django Imports
from django.core.cache import cache

# Rest Framework Imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Local Imports
from core.choices import QUALIFICATION_CHOICES, SPECIALIZATION_CHOICES


class ProfileChoiceView(APIView):
    def post(self, request):
        """
        Get the user profile choice
        """

        choices = cache.get("profile_choices")
        get_cache = request.data.get("get_cache", False)

        if not choices or get_cache:
            qualification_choices = [
                {"value": choice[0], "label": choice[1]}
                for choice in QUALIFICATION_CHOICES
            ]
            specialization_choices = [
                {"value": choice[0], "label": choice[1]}
                for choice in SPECIALIZATION_CHOICES
            ]

            choices = {
                "qualification": qualification_choices,
                "specialization": specialization_choices,
            }

            cache.set("profile_choices", choices, timeout=60 * 60 * 24 * 7)

        return Response(choices, status=status.HTTP_200_OK)
