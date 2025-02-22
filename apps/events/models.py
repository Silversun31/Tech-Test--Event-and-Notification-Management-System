from django.db import models

# Create your models here.
from django.db import models
from apps.core.models import BaseModel


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
