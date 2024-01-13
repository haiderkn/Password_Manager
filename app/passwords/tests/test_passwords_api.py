"""
Tests for the passwords API
"""
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core import models
from passwords import serializers


PASSWORDS_LIST_URL = reverse('passwords:credential-list')
PASSWORDS_DETAILS_URL = reverse('passwords:credential-detail', args=[1])

class PublicPasswordsApiTests(TestCase):
    """Test the publicly available passwords API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving passwords"""
        res = self.client.get(PASSWORDS_LIST_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_required_for_create(self):
        """Test that login is required for creating passwords"""
        res = self.client.post(PASSWORDS_LIST_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_required_for_edit(self):
        """Test that login is required for editing passwords"""
        res = self.client.put(PASSWORDS_DETAILS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
