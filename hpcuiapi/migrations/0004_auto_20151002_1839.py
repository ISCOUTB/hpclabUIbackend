# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpcuiapi', '0003_auto_20150921_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='description',
        ),
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=600, null=True),
        ),
    ]
