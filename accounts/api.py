from django.contrib.auth.models import User,auth
from rest_framework import viewsets,status
from .serializers import RegistrationSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class Registrationlist(APIView):
    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
