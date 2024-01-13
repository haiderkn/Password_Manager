"""
views for the passwords APIs
"""
from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import permissions

from passwords import serializers
from core.models import LoginCredential


class CredentialViewset(viewsets.ModelViewSet):
    """
    Viewset for the LoginCredential model
    """
    serializer_class = serializers.LoginCredentialSerializer
    queryset = LoginCredential.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        Return objects for the current authenticated user only
        """
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
