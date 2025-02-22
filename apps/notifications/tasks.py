from celery import shared_task
from django.utils.timezone import now
from .models import Notification
from apps.events.models import Event


@shared_task
def send_event_notification(event_id, action):
    """
    Asynchronous task to log a notification when an event is created or updated.
    """
    event = Event.objects.filter(id=event_id, is_deleted=False).first()
    if not event:
        return f"Event {event_id} not found or deleted."

    message = f"The event '{event.title}' has been {action} on {now().strftime('%Y-%m-%d %H:%M:%S')}."

    Notification.objects.create(event=event, message=message)
    return f"Notification recorded: {message}"
