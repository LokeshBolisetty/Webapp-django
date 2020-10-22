from rest_framework.views import APIView
from .models import mentor, Course
from rest_framework.response import Response
from .serializers import Courseserializer,mentorserializer
from rest_framework import status


class mentorlist(APIView):
    def get(self,request):
        model = mentor.objects.all()
        serializer = mentorserializer(model,many=True)
        return Response(serializer.data)
    
    def post(self,request):
    
        serializer = mentorserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class mentorid(APIView):
    def get(self,request,mentor_id):
        model = mentor.objects.filter(id__exact=mentor_id)
        if model:
            serializer = mentorserializer(model,many=True)
            return Response(serializer.data)
        else:
            return Response(f"Mentor doesn't exist with id {mentor_id}",status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,mentor_id):
        try:
            model = mentor.objects.get(id=mentor_id)
        except:
            return Response(f"Mentor doesn't exist with id {mentor_id}",status=status.HTTP_404_NOT_FOUND)
        if model:
            serializer = mentorserializer(model,data=request.data)
            #if not request.data["name"]:
            #    request.data["name"] = model.name
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
        
    def delete(self,request,mentor_id):
        try:
            model = mentor.objects.get(id=mentor_id)
        except:
            return Response(f"Mentor doesn't exist with id {mentor_id}",status=status.HTTP_404_NOT_FOUND)

        model.delete()
        return Response(status=status.HTTP_200_OK)
      
 

class Courselist(APIView):
    def get(self,request):
        model = Course.objects.all()
        serializer = Courseserializer(model,many=True)
        return Response(serializer.data)

    def post(self,request):
    
        serializer = Courseserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class courseid(APIView):
    def get(self,request,course_id):
        model = Course.objects.filter(id__exact=course_id)
        if model:
            serializer = Courseserializer(model,many=True)
            return Response(serializer.data)
        else:
            return Response(f"Course doesn't exist with id {course_id}",status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,course_id):
        try:
            model = Course.objects.get(id=course_id)
        except:
            return Response(f"Course doesn't exist with id {course_id}",status=status.HTTP_404_NOT_FOUND)
        if model:
            serializer = Courseserializer(model,data=request.data)
            #As of now mentor column has to be passed always.
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
        
    def delete(self,request,course_id):
        try:
            model = course.objects.get(id=course_id)
        except:
            return Response(f"course doesn't exist with id {course_id}",status=status.HTTP_404_NOT_FOUND)

        model.delete()
        return Response(status=status.HTTP_200_OK)