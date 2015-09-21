from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=140, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.creator.username, filename)


class File(models.Model):
    creator = models.ForeignKey(User)
    description = models.CharField(max_length=140, null=True)
    file = models.FileField(upload_to=user_directory_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
