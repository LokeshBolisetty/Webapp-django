from rest_framework.views import APIView
from .models import mentor, Course
from rest_framework.response import Response
from .serializers import Courseserializer,mentorserializer
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

#The folling decorator has been added to try and remove csrf validation error but it did not succeed
@method_decorator(csrf_exempt, name='dispatch')
class mentorlist(APIView):
    #authentication_classes and permission_classes make sure that the user is logged in to access the mentors list.
    authentication_classes = [SessionAuthentication,TokenAuthentication]
    permission_classes = [IsAuthenticated]
    #This is the overriden method to GET the list of all the mentors. Works only if the user is logged in.
    def get(self,request):
        model = mentor.objects.all()
        serializer = mentorserializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
    #This is the overriden method to POST a new mentor. Works only if the user is logged in.
        serializer = mentorserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class mentorid(APIView):
    #This method returns the mentor by his id and returns only that particular mentor.
    def get(self,request,mentor_id):
        #This is the line which filters the mentors to get the required particular mentor.
        model = mentor.objects.filter(id__exact=mentor_id)
        if model:
            serializer = mentorserializer(model,many=True)
            return Response(serializer.data)
        else:
            return Response(f"Mentor doesn't exist with id {mentor_id}",status=status.HTTP_404_NOT_FOUND)

    #This method can be used to update the existing mentor. Only those fields which have to changed can be given. Others are set to their initial values.
    def put(self,request,mentor_id):
        try:
            model = mentor.objects.get(id=mentor_id)
        except:
            return Response(f"Mentor doesn't exist with id {mentor_id}",status=status.HTTP_404_NOT_FOUND)
        if model:
            #This fetches the data from mentorlistserializer
            serializer = mentorserializer(model,data=request.data)
            # If name is given request.data.get('name',0) evaualtes to value in name otherwise it takes the value of zero. 
            # This is done to set the value of name to the already existing name in the database if new value for name is not provided by the user.
            # Similar logic is applied for all the fields.
            if request.data.get('name',0) == 0:
                request.data['name'] = model.name
            if request.data.get('id',0) == 0:
                request.data['id'] = model.id
            if request.data.get('age',0) == 0:
                request.data['age'] = model.age
            if serializer.is_valid():
                serializer.save()
                
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #To delete a mentor from the list of mentors.
    def delete(self,request,mentor_id):
        try:
            model = mentor.objects.get(id=mentor_id)
        except:
            return Response(f"Mentor doesn't exist with id {mentor_id}",status=status.HTTP_404_NOT_FOUND)

        model.delete()
        return Response(status=status.HTTP_200_OK)
      
 

class Courselist(APIView):
    #This methods returns all the courses that are in the database.
    def get(self,request):
        model = Course.objects.all()
        #Uses the courseserializer from serializers file in this app
        serializer = Courseserializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        #Allows the addition of new course. Authentication has to be added
        serializer = Courseserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class courseid(APIView):
    #This returns a course with a particular id.
    def get(self,request,course_id):
        model = Course.objects.filter(id__exact=course_id)
        if model:
            serializer = Courseserializer(model,many=True)
            return Response(serializer.data)
        else:
            return Response(f"Course doesn't exist with id {course_id}",status=status.HTTP_404_NOT_FOUND)
    #Any change that has to be made to the course can be done using this method.
    def put(self,request,course_id):
        try:
            model = Course.objects.get(id=course_id)
        except:
            return Response(f"Course doesn't exist with id {course_id}",status=status.HTTP_404_NOT_FOUND)
        if model:
            serializer = Courseserializer(model,data=request.data)
            #As of now mentor column has to be passed always.
            #This lines of code are to make sure that the api does not give error even if some of the fields are not passed while updating the course.
            if request.data.get('title',0) == 0:
                request.data['title'] = model.title
            if request.data.get('id',0) == 0:
                request.data['id'] = model.id
            if request.data.get('description',0) == 0:
                request.data['description'] = model.description
            if request.data.get('mentor',0) == 0:
                request.data['mentor'] = model.mentor
            if serializer.is_valid():
                print(request.data['mentor'])
                serializer.save()
                
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #Method to delete the course by its id.
    def delete(self,request,course_id):
        try:
            model = course.objects.get(id=course_id)
        except:
            return Response(f"course doesn't exist with id {course_id}",status=status.HTTP_404_NOT_FOUND)

        model.delete()
        return Response(status=status.HTTP_200_OK)
