from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """
    Custom view to ensure the returned token has the 'Bearer ' prefix.
    """
    serializer_class = CustomTokenObtainPairSerializer
