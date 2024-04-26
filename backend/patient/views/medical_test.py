from rest_framework.generics import ListAPIView

from patient.models import MedicalTest
from patient.serializers import MedicalTestSerializer


class MedicalTestListView(ListAPIView):
    """
    View to list all the medical tests.
    """

    queryset = MedicalTest.objects.all()
    serializer_class = MedicalTestSerializer
