# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0010_auto_20150716_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.CharField(max_length=100, unique=True, db_index=True),
        ),
    ]
