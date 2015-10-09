# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpcuiapi', '0004_auto_20151002_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='filename',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='size',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
