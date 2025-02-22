from apps.core.serializers import BaseSerializer
from .models import Notification


class NotificationSerializer(BaseSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
