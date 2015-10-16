# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpcuiapi', '0007_auto_20151014_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='filename',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='type',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=768, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='tool',
            name='description',
            field=models.CharField(max_length=768, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(max_length=256),
        ),
    ]
