from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, RegistrationViewSet

router = DefaultRouter()
router.register(r"events", EventViewSet, basename="event")
router.register(r"registrations", RegistrationViewSet, basename="registration")

urlpatterns = [
    path("", include(router.urls)),
    path("registrations/register/", RegistrationViewSet.as_view({"post": "register"}), name="register"),
    path("registrations/cancel/", RegistrationViewSet.as_view({"post": "cancel"}), name="cancel"),
]
