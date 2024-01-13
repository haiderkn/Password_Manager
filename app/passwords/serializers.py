from rest_framework import serializers
from core.models import LoginCredential


class LoginCredentialSerializer(serializers.ModelSerializer):
    """Serializer for LoginCredential objects."""

    class Meta:
        model = LoginCredential
        fields = ('id', 'link', 'email', 'password')
        read_only_fields = ('id',)