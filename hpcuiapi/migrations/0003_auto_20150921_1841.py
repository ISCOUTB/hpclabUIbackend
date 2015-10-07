# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpcuiapi', '0002_auto_20150921_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='path',
            new_name='file',
        ),
    ]
