from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.events.models import Event
from .tasks import send_event_notification


@receiver(post_save, sender=Event)
def event_notification_handler(sender, instance, created, **kwargs):
    """
    Triggers a notification when an event is created or updated.
    """
    action = "created" if created else "updated"
    send_event_notification.delay(instance.id, action)
