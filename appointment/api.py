from rest_framework.views import APIView
from .models import Appointment
from rest_framework.response import Response
from .serializers import Appointmentserilizer
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class Appointmentlist(APIView):
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        model = Appointment.objects.all()
        serializer = Appointmentserilizer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
    
        serializer = Appointmentserilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class Appointmentid(APIView):
    def get(self,request,id):
        model = Appointment.objects.filter(id__exact=id)
        if model:
            serializer = Appointmentserilizer(model,many=True)
            return Response(serializer.data)
        else:
            return Response(f"Appointment doesn't exist with id {id}",status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,id):
        try:
            model = Appointment.objects.get(id=id)
        except:
            return Response(f"Appointment doesn't exist with id {id}",status=status.HTTP_404_NOT_FOUND)
        if model:
            serializer = Appointmentserilizer(model,data=request.data)
            print(model.id)
            print(model)
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
        
    def delete(self,request,id):
        try:
            model = Appointment.objects.get(id=id)
        except:
            return Response(f"Appointment doesn't exist with id {id}",status=status.HTTP_404_NOT_FOUND)

        model.delete()
        return Response(status=status.HTTP_200_OK)

class Appointmentuserid(APIView):
    def get(self,request,user_id):
        model = Appointment.objects.filter(user__exact=user_id)
        if model:
            serializer = Appointmentserilizer(model,many=True)
            return Response(serializer.data)
        else:
            return Response(f"User doesn't exist with id {user_id}",status=status.HTTP_404_NOT_FOUND)

class Appointmentmentorid(APIView):
    def get(self,request,mentor_id):
        model = Appointment.objects.filter(appointment_with__exact=mentor_id)
        if model:
            serializer = Appointmentserilizer(model,many=True)
            return Response(serializer.data)
        else:
            return Response(f"Mentor doesn't exist with name {mentor_id}",status=status.HTTP_404_NOT_FOUND)

      
 

