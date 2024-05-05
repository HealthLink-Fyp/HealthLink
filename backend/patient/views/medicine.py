from rest_framework.generics import ListAPIView

from patient.models import MedicineShop
from patient.serializers import MedicineShopSerializer

from rest_framework.response import Response


from rest_framework.response import Response


class MedicineListView(ListAPIView):
    """
    View to list all the manufacturers of the medicines.
    """

    serializer_class = MedicineShopSerializer
    filter = ("name", "manufacturer")
    lookup_field = "medicine_id"

    def get(self, request, *args, **kwargs):
        manufacturers = request.query_params.get("manufacturers")

        if manufacturers:
            queryset = (
                self.get_queryset().values_list("manufacturer", flat=True).distinct()
            )
            return Response({"counts": len(queryset), "manufacturers": list(queryset)})

        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        medicine_id = self.kwargs.get("medicine_id", None)
        queryset = MedicineShop.objects.all()

        if medicine_id:
            self.pagination_class = None
            return queryset.filter(medicine_id=medicine_id)

        for field in self.filter:
            value = self.request.query_params.get(field)

            if value:
                queryset = queryset.filter(**{field: value})

        return queryset
