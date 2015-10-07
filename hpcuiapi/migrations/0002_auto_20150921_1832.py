# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hpcuiapi.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hpcuiapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=140, null=True)),
                ('path', models.FileField(upload_to=hpcuiapi.models.user_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
