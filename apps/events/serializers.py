from .models import Event
from ..core.serializers import BaseSerializer


class EventSerializer(BaseSerializer):
    class Meta:
        model = Event
        fields = "__all__"
