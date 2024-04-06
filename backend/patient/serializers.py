from rest_framework.serializers import ModelSerializer
from .models import Appointment


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"
