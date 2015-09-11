__author__ = 'juan'
from rest_framework import serializers
from hpcuiapi.models import Project
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('username', 'password', )


class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    creator = UserSerializer(required=False)
    class Meta:
        model = Project
