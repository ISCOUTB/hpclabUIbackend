# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpcuiapi', '0005_auto_20151002_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
        migrations.AddField(
            model_name='file',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='filename',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
