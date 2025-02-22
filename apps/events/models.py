from django.db import models

# Create your models here.
from django.db import models
from apps.core.models import BaseModel
from apps.users.models import CustomUser
from config import settings


class Event(BaseModel):
    """Event Model"""
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    class Meta:
        ordering = ["start_datetime"]

    def __str__(self):
        return self.title


class Registration(BaseModel):
    """Registration Model."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="registrations")
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "event")

    def __str__(self):
        return f"{self.event.title} - {self.user.username}"
