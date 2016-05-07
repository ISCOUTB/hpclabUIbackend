# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hpcuiapi', '0002_auto_20160330_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workflowstep',
            name='id',
        ),
        migrations.AddField(
            model_name='workflowstep',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 30, 22, 29, 56, 498879, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workflowstep',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 30, 22, 30, 7, 98284, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workflowstep',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
    ]
