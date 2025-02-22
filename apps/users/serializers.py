from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom serializer to add the 'Bearer ' prefix to the token in the login response.
    """

    def validate(self, attrs):
        data = super().validate(attrs)
        data["access"] = f"Bearer {data['access']}"
        return data
