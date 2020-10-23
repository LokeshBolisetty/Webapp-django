from rest_framework.views import APIView
from .models import Appointment
from rest_framework.response import Response
from .serializers import Appointmentserilizer
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#This is the class which extends APIView from django rest framework. Usage of this class need authentication i.e the user has to be signed it to use this class.
# This allows user to book a one on one appointment with mentor.
class Appointmentlist(APIView):
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    #This is the overriden method get from APIView class. It displays all the appointments that are scheduled.
    def get(self,request):
        model = Appointment.objects.all()
        serializer = Appointmentserilizer(model,many=True)
        return Response(serializer.data)
    
    #This method allows you to make a new appointment.
    def post(self,request):
    
        serializer = Appointmentserilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Appointmentid(APIView):
    #This method displays only those appointments which match with the given id. If there is no such appointment it gives 404
    def get(self,request,id):
        model = Appointment.objects.filter(id__exact=id)
        if model:
            serializer = Appointmentserilizer(model,many=True)
            return Response(serializer.data)
        else:
            return Response(f"Appointment doesn't exist with id {id}",status=status.HTTP_404_NOT_FOUND)
    #This method allows user to modify the appoitntment. Any field that is not given by the user will be set to the previous values.
    def put(self,request,id):
        try:
            model = Appointment.objects.get(id=id)
        except:
            return Response(f"Appointment doesn't exist with id {id}",status=status.HTTP_404_NOT_FOUND)
        if model:
            serializer = Appointmentserilizer(model,data=request.data)
            # print(model.id)
            # print(model)
            #if not request.data["name"]:
            #    request.data["name"] = model.name
            if request.data.get('user',0) == 0:
                request.data['user'] = model.user_id
            # if request.data.get('id',0) == 0:
            #     request.data['id'] = model.id
            if request.data.get('time_start',0) == 0:
                request.data['time_start'] = model.time_start
            if request.data.get('time_end',0) == 0:
                request.data['time_end'] = model.time_end
            if request.data.get('date',0) == 0:
                request.data['date'] = model.date
            if request.data.get('room_number',0) == 0:
                request.data['room_number'] = model.room_number
            if request.data.get('appointment_with',0) == 0:
                request.data['appointment_with'] = model.appointment_with
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #This method allows user to delete an existing appointment by its id   
    def delete(self,request,id):
        try:
            model = Appointment.objects.get(id=id)
        except:
            return Response(f"Appointment doesn't exist with id {id}",status=status.HTTP_404_NOT_FOUND)

        model.delete()
        return Response(status=status.HTTP_200_OK)

class Appointmentuserid(APIView):
    #This method prints the appointments of a particular customer by his ID.
    def get(self,request,user_id):
        model = Appointment.objects.filter(user__exact=user_id)
        if model:
            serializer = Appointmentserilizer(model,many=True)
            return Response(serializer.data)
        else:
            return Response(f"User doesn't exist with id {user_id}",status=status.HTTP_404_NOT_FOUND)

class Appointmentmentorid(APIView):
    #This method prints the appointments of a particular mentor by his name.
    def get(self,request,mentor_id):
        model = Appointment.objects.filter(appointment_with__exact=mentor_id)
        if model:
            serializer = Appointmentserilizer(model,many=True)
            return Response(serializer.data)
        else:
            return Response(f"Mentor doesn't exist with name {mentor_id}",status=status.HTTP_404_NOT_FOUND)

      
 

