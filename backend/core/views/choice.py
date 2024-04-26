# Rest Framework Imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Local Imports
from core.choices import (
    ROLE_CHOICES as RC,
    QUALIFICATION_CHOICES as QC,
    SPECIALIZATION_CHOICES as SPC,
    APPOINTMENT_STATUS_CHOICES as SC,
    DAY_CHOICES as DC,
)


class ProfileChoiceView(APIView):
    def get(self, request):
        """
        Get the user profile choice
        """

        def get_choices(choices):
            return [{"value": choice[0], "label": choice[1]} for choice in choices]

        choices = {
            "qualification": get_choices(QC),
            "specialization": get_choices(SPC),
            "status": get_choices(SC),
            "day": get_choices(DC),
            "role": get_choices(RC),
        }

        return Response(choices, status=status.HTTP_200_OK)
