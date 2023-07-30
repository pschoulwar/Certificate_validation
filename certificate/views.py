from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from .serializers import CertificateSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class CreateCertificate(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = CertificateSerializer(data=request.data)
        if serializer.is_valid():
            certificate = serializer.save()
            serialized_data = CertificateSerializer(certificate).data
            return Response({
                'message': 'Certificate Created Successfully',
                'data': serialized_data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

class ValidateCertificate(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        name = request.data.get('name')
        certificate_number = request.data.get('certificate_number')
        
        try:
            certificate = models.Certificate.objects.get(name=name, certificate_number=certificate_number)
            is_valid_certificate = True
            
        except models.Certificate.DoesNotExist:
            is_valid_certificate = False
          
        if   is_valid_certificate:
            return Response({'message':'certificate is valid'}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'certificate is invalid'}, status=status.HTTP_200_OK)

            
