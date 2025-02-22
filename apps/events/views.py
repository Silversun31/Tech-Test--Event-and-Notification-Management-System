# Create your views here.
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from .models import Event
from .serializers import EventSerializer
from .services import get_filtered_events


class EventPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class EventViewSet(viewsets.ModelViewSet):
    """
    CRUD for event management.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = EventPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        filtered_events = get_filtered_events(request.query_params)
        paginated_queryset = self.paginate_queryset(filtered_events)
        serializer = self.get_serializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)
