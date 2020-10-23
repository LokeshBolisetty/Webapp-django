from rest_framework import serializers
from  .models import mentor, Course


class mentorserializer(serializers.ModelSerializer):
    #Serializer converts SQL data to JSON data.
    #__all__ in 'fields' parses all the fields
    class Meta:
        model = mentor
        fields = '__all__'

class Courseserializer(serializers.ModelSerializer):
    #__all__ is not used in fields because we want mentors name also to be displayed. The method corresponding to printing the names instead of IDs is also included in the 'fields'
    class Meta:
        model = Course
        #fields = '__all__'
        fields = ['title','description','mentors',"mentor"]
        