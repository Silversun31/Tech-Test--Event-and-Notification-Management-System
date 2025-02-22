import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from apps.events.models import Event


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_user(db):
    """Create a test user."""
    User = get_user_model()
    return User.objects.create_user(username="testuser", password="testpass")


@pytest.fixture
def test_event(db):
    """Create a test event."""
    return Event.objects.create(
        title="Test event",
        description="Test description",
        location="Madrid",
        start_datetime="2025-03-01T10:00:00Z",
        end_datetime="2025-03-01T12:00:00Z"
    )


def test_create_event(api_client, test_user):
    """Test event creation."""
    api_client.force_authenticate(user=test_user)
    response = api_client.post("/api/events/", {
        "title": "New event",
        "description": "Event description",
        "location": "Barcelona",
        "start_datetime": "2025-04-01T10:00:00Z",
        "end_datetime": "2025-04-01T12:00:00Z"
    })
    assert response.status_code == 201
    assert response.data["title"] == "New event"


def test_list_events(api_client, test_event):
    """Test event list retrieval."""
    response = api_client.get("/api/events/")
    assert response.status_code == 200
    assert len(response.data["results"]) > 0


def test_update_event(api_client, test_user, test_event):
    """Test event update."""
    api_client.force_authenticate(user=test_user)
    response = api_client.patch(f"/api/events/{test_event.id}/", {"title": "Updated event"})
    assert response.status_code == 200
    assert response.data["title"] == "Updated event"


def test_delete_event(api_client, test_user, test_event):
    """Test event soft delete."""
    api_client.force_authenticate(user=test_user)
    response = api_client.delete(f"/api/events/{test_event.id}/")
    assert response.status_code == 204
    assert not Event.objects.filter(id=test_event.id).exists()
