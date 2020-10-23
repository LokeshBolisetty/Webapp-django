from rest_framework import serializers
from  .models import Appointment

#Serializer parses SQL data to JSON to facilitate usage in web apps.
class Appointmentserilizer(serializers.ModelSerializer):
    #__all__ in fields parse all the fields in the Appointment model imported from models.py in this app
    class Meta:
        model = Appointment
        fields = '__all__'

        