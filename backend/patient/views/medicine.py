from rest_framework.generics import ListAPIView

from patient.models import MedicineShop
from patient.serializers import MedicineShopSerializer


class MedicineListView(ListAPIView):
    """
    View to list all the medicines.
    """

    queryset = MedicineShop.objects.all()
    serializer_class = MedicineShopSerializer
