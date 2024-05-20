from .models import Call, Chat

from rest_framework import serializers


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = "__all__"


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"
