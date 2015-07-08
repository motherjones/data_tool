# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20150708_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='active',
            field=models.BooleanField(db_index=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='bounces',
            field=models.IntegerField(db_index=True),
        ),
    ]
