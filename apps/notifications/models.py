from django.db import models
from apps.core.models import BaseModel
from apps.events.models import Event


class Notification(BaseModel):
    """Model to store simulated notifications."""
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Notification for {self.event.title}: {self.message[:50]}"
