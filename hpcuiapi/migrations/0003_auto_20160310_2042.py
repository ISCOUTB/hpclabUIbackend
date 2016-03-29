# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hpcuiapi', '0002_auto_20160209_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=768, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='params',
            field=jsonfield.fields.JSONField(null=True, blank=True),
        ),
    ]
