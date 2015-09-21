from rest_framework import serializers
from models import Project, File
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False, allow_null=True)
    creator = UserSerializer(required=False)

    class Meta:
        model = Project


class FileSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    file = serializers.FileField(required=True)
    size = serializers.IntegerField(required=False)

    class Meta:
        model = File
