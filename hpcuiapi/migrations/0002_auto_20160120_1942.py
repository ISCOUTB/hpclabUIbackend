# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import hpcuiapi.models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hpcuiapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ForeignKey(to='hpcuiapi.File')),
                ('project', models.ForeignKey(to='hpcuiapi.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ToolFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(storage=hpcuiapi.models.MediaFileSystemStorage(), upload_to=b'tools')),
                ('exe', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkflowStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('params', jsonfield.fields.JSONField()),
                ('input', models.ForeignKey(blank=True, to='hpcuiapi.WorkflowStep', null=True)),
                ('project', models.ForeignKey(to='hpcuiapi.Project')),
            ],
        ),
        migrations.AlterField(
            model_name='tool',
            name='params',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='workflowstep',
            name='tool',
            field=models.ForeignKey(to='hpcuiapi.Tool'),
        ),
        migrations.AddField(
            model_name='toolfile',
            name='tool',
            field=models.ForeignKey(to='hpcuiapi.Tool'),
        ),
    ]
