# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0008_auto_20150716_0018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='code',
            field=models.CharField(db_index=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='signup',
            name='group',
            field=models.CharField(db_index=True, max_length=200),
        ),
    ]
