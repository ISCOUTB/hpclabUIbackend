# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hpcuiapi', '0003_auto_20160310_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='params',
            field=jsonfield.fields.JSONField(default=[]),
        ),
        migrations.AlterField(
            model_name='workflowstep',
            name='params',
            field=jsonfield.fields.JSONField(default=[]),
        ),
    ]
