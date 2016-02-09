from rest_framework import serializers
from models import Project, File, Tool, ToolFile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff')


class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Project


class FileSerializer(serializers.ModelSerializer):
    filename = serializers.CharField(required=False)
    file = serializers.FileField(required=True)
    size = serializers.IntegerField(required=False)
    md5sum = serializers.CharField(required=False)

    class Meta:
        model = File


class JSONSerializerField(serializers.Field):

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class ToolSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    params = JSONSerializerField(required=False)

    class Meta:
        model = Tool


class ToolFileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)
    filename = serializers.CharField(required=False)
    size = serializers.IntegerField(required=False)
    exe = serializers.BooleanField(required=True)

    class Meta:
        model = ToolFile