from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from ..events.views import BasePagination


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only ViewSet to list notifications.
    """
    queryset = Notification.objects.all().order_by("-created_at")
    serializer_class = NotificationSerializer
    pagination_class = BasePagination
    permission_classes = [IsAuthenticated]
