# Create your models here.

from django.db import models
from django.utils.timezone import now


class TraceabilityMixin(models.Model):
    """Mixin to track creation and update of records."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteQuerySet(models.QuerySet):
    """QuerySet that automatically filters out deleted objects."""

    def alive(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)


class SoftDeleteManager(models.Manager):
    """Custom manager that uses the SoftDeleteQuerySet."""

    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).alive()


class SoftDeleteMixin(models.Model):
    """Mixin for soft delete with custom manager."""
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = now()
        self.save(update_fields=["is_deleted", "deleted_at"])

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save(update_fields=["is_deleted", "deleted_at"])

    class Meta:
        abstract = True


class BaseModel(TraceabilityMixin, SoftDeleteMixin):
    """Base model for the application, including tracking and soft delete."""

    class Meta:
        abstract = True
