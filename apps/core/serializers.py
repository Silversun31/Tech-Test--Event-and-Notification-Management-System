from rest_framework import serializers


class ExcludeSoftDeleteMixin:
    """
        Mixin that automatically excludes soft delete fields
        in DRF serializers.
    """

    def get_fields(self):
        fields = super().get_fields()
        fields.pop("is_deleted", None)
        fields.pop("deleted_at", None)
        return fields


class BaseSerializer(ExcludeSoftDeleteMixin, serializers.ModelSerializer):
    """
    Base serializer for all application models.
    """

    class Meta:
        abstract = True
