from django.contrib.auth.models import User,auth
from rest_framework import viewsets,status
from .serializers import RegistrationSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

#This is an extended class of the APIView class from django rest framework
class Registrationlist(APIView):
    #It has only one method overriden. It uses the RegistrationSerializer from serializers file in this app to change the data.
    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        #Saves the data given if it is in the valid format. Otherwise gives appropriate error.
        if serializer.is_valid():
            serializer.save()
            #If executed successfully it gives a response saying that changes have been made successfully.
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        #If execution is not possible, it gives response saying its a bad request.
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
