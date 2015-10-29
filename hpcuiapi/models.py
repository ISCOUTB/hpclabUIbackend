from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
from django.core.files.storage import FileSystemStorage
from django.dispatch import receiver
import os
import hashlib


class MediaFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name):
        return name

    def _save(self, name, content):
        if self.exists(name):
            return name
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


@receiver(models.signals.post_delete, sender=File)
def md5based_delete_file(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            md5 = hashlib.md5()
            for chunk in instance.file.chunks():
                md5.update(chunk)
            md5code = md5.hexdigest()
            if File.objects.filter(md5sum=md5code).count() == 0:
                os.remove(instance.file.path)


class Tool(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=768, null=True)
    params = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

