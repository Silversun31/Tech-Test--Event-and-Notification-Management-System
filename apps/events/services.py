from django.db.models import Q
from django.utils.timezone import now
from rest_framework.exceptions import ValidationError
from .models import Registration, Event


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


def register_user_to_event(user, event_id):
    """
    Registers a user to an event, validating duplicates and that the event is active.
    """
    event = Event.objects.filter(id=event_id, is_deleted=False).first()
    if not event:
        raise ValidationError("The event does not exist or has been deleted.")

    if event.start_datetime < now():
        raise ValidationError("You cannot register for an event that has already started.")

    if Registration.objects.filter(user=user, event=event).exists():
        raise ValidationError("Your are already registered for this event.")

    registration = Registration.objects.create(user=user, event=event)
    return registration


def cancel_registration(user, event_id):
    """
    Cancels a user's registration for an event.
    """
    registration = Registration.objects.filter(user=user, event_id=event_id).first()
    if not registration:
        raise ValidationError("You are not registered for this event or it has already been canceled.")

    registration.delete()
    return registration
