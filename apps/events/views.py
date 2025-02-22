# Create your views here.
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer
from .services import get_filtered_events, register_user_to_event, cancel_registration


class BasePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class EventViewSet(viewsets.ModelViewSet):
    """
    CRUD for event management.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = BasePagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        filtered_events = get_filtered_events(request.query_params)
        paginated_queryset = self.paginate_queryset(filtered_events)
        serializer = self.get_serializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)


class RegistrationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    """
    CRUD for event registration management.
    """
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    pagination_class = BasePagination
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"])
    def register(self, request):
        """
        Register a user for an event.
        """
        user = request.user
        event_id = request.data.get("event_id")

        if not event_id:
            raise ValidationError("You must provide an event_id.")

        registration = register_user_to_event(user, event_id)
        serializer = self.get_serializer(registration)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"])
    def cancel(self, request):
        """
        Cancel a user's registration for an event.
        """
        user = request.user
        event_id = request.data.get("event_id")

        if not event_id:
            raise ValidationError("You must provide an event_id.")

        cancel_registration(user, event_id)
        return Response({"message": "Registration successfully canceled."}, status=status.HTTP_200_OK)
