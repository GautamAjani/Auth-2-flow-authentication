from .models import User
from rest_framework import serializers
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate
from datetime import datetime
import pdb

class UserSerializer(serializers.ModelField):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'token', 'refresh_token']


    def create(self, validated_data):
        return User.objects.create(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)


    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user_obj = User.objects.filter(email=email).first()
        user = authenticate(username=email, password=password)
        token  = user.token
        user.refresh_token = token
        user.save()
        return {
            'email': user.email,
            'token': token,
        }
