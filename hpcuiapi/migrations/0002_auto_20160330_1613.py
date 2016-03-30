# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hpcuiapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workflowstep',
            name='input',
        ),
        migrations.AddField(
            model_name='workflowstep',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
