from rest_framework import serializers
from  .models import mentor, Course

class mentorserializer(serializers.ModelSerializer):
    class Meta:
        model = mentor
        fields = '__all__'

class Courseserializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        #fields = '__all__'
        fields = ['title','description','mentors',"mentor"]
        