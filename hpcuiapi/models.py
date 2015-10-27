from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
from django.core.files.storage import FileSystemStorage
import os
import hashlib


class MediaFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name):
        return name

    def _save(self, name, content):
        if self.exists(name):
            # if the file exists, do not call the superclasses _save method
            return name
        # if the file is new, DO call it
        return super(MediaFileSystemStorage, self)._save(name, content)


class Project(models.Model):
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=768, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def media_file_name(instance, filename):
    h = instance.md5sum
    basename, ext = os.path.splitext(filename)
    return os.path.join('mediafiles', h[0:1], h[1:2], h + ext.lower())


class File(models.Model):
    creator = models.ForeignKey(User)
    filename = models.CharField(max_length=256, null=True)
    file = models.FileField(upload_to=media_file_name, storage=MediaFileSystemStorage())
    md5sum = models.CharField(max_length=36)
    size = models.IntegerField(null=True)
    type = models.CharField(max_length=256, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            md5 = hashlib.md5()
            for chunk in self.file.chunks():
                md5.update(chunk)
            self.md5sum = md5.hexdigest()
        super(File, self).save(*args, **kwargs)


class Tool(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=768, null=True)
    params = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

