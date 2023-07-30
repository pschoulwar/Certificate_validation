from django.urls import path
from .views import CreateCertificate, ValidateCertificate

urlpatterns = [
    path('create_certificate/', CreateCertificate.as_view(), name='create_certificate'),
    path('validate_certificate/', ValidateCertificate.as_view(), name='validate_certificate'),
]
