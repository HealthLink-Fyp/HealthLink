from rest_framework.generics import ListAPIView

from patient.models import MedicalTest
from patient.serializers import MedicalTestSerializer


class MedicalTestListView(ListAPIView):
    """
    View to list all the medical tests.
    """

    queryset = MedicalTest.objects.all()
    serializer_class = MedicalTestSerializer
    filter = ("name", "lab_name")

    def get_queryset(self):
        test_id = self.kwargs.get("test_id", None)
        queryset = MedicalTest.objects.all()

        if test_id:
            self.pagination_class = None
            return queryset.filter(test_id=test_id)

        for field in self.filter:
            value = self.request.query_params.get(field)

            if value:
                queryset = queryset.filter(**{field: value})

        return queryset
