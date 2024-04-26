from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from patient.serializers import EmotionSerializer


class EmotionView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = EmotionSerializer(data=request.data)

        # No database model for this serializer
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={"uint_array": serializer.data["uint_array"]},
            status=status.HTTP_201_CREATED,
        )
