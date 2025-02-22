from django.db.models import Q
from .models import Event


def get_filtered_events(query_params):
    """
    Returns events filtered by date or location.
    """
    events = Event.objects.all()

    start_date = query_params.get("start_date")
    end_date = query_params.get("end_date")
    location = query_params.get("location")

    if start_date and end_date:
        events = events.filter(start_datetime__range=[start_date, end_date])

    if location:
        events = events.filter(Q(location__icontains=location))

    return events
