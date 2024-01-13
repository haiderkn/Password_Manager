from django.urls import path, include
from passwords.views import CredentialViewset


app_name = 'passwords'

urlpatterns = [
    path('', CredentialViewset.as_view({'get': 'list', 'post': 'create'}), name='credential-list'),
    path('<int:pk>/', CredentialViewset.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='credential-detail'),
]