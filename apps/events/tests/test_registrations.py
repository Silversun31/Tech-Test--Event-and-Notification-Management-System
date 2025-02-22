import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from apps.events.models import Event, Registration


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_user(db):
    User = get_user_model()
    return User.objects.create_user(username="testuser", password="testpass")


@pytest.fixture
def test_event(db):
    return Event.objects.create(
        title="Test event",
        description="Test description",
        location="Madrid",
        start_datetime="2025-03-01T10:00:00Z",
        end_datetime="2025-03-01T12:00:00Z"
    )


def test_register_event(api_client, test_user, test_event):
    """Test event registration."""
    api_client.force_authenticate(user=test_user)
    response = api_client.post("/api/registrations/register/", {"event_id": test_event.id})
    assert response.status_code == 201
    assert Registration.objects.filter(user=test_user, event=test_event).exists()


def test_cancel_registration(api_client, test_user, test_event):
    """Test event registration cancellation."""
    api_client.force_authenticate(user=test_user)
    Registration.objects.create(user=test_user, event=test_event)
    response = api_client.post("/api/registrations/cancel/", {"event_id": test_event.id})
    assert response.status_code == 200
    assert not Registration.objects.filter(user=test_user, event=test_event).exists()
