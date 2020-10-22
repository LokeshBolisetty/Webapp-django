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

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','password','email','is_staff']
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']