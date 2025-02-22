from rest_framework import serializers

from .models import Event
from ..core.serializers import BaseSerializer
from .models import Registration


class EventSerializer(BaseSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class RegistrationSerializer(BaseSerializer):
    event_id = serializers.IntegerField(write_only=True)
    event = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Registration
        fields = ["id", "user", "event", "event_id", "registered_at"]
