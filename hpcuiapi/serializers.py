from rest_framework import serializers
from models import Project, File
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False, allow_null=True)
    creator = UserSerializer(required=False)

    class Meta:
        model = Project


class FileSerializer(serializers.ModelSerializer):
    filename = serializers.CharField(required=False)
    file = serializers.FileField(required=True)
    size = serializers.IntegerField(required=False)

    class Meta:
        model = File
