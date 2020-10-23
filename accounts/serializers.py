from rest_framework import serializers
#from .models import Account
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# class UserSerializer(serializers.ModelSerializer):
#     def create(self, *args, **kwargs):
#         user = super().create(*args, **kwargs)
#         p = user.password
#         user.set_password(p)
#         user.save()
#         return user

#     def update(self, *args, **kwargs):
#         user = super().update(*args, **kwargs)
#         p = user.password
#         user.set_password(p)
#         user.save()
#         return user

#     class Meta:
#         model = get_user_model()

# This is the RegistrationSerializer that will be used in api.py
# It extends the ModelSerializer class from django rest framework.
# Serializer converts sql data to json data facilitating the use in web apps
# It takes data from the User table in the database and parses the fields mentioned in 'fields' Any extra fields required can be added there itself.
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','email','is_staff']
    #These are overriden methods given by django itself. They are used so that when new user is added, his password is saved after encrypting. 
    #One can add methods to directly add users to the User model. But passwords will not be crypted.
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    #Password changes are taken care of
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

#This can be used to log in to one's account. This uses username and password to login. It can be changed to emaial and password or anything else too if required.
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']