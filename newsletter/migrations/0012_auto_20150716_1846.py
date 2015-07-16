# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0011_auto_20150716_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='active',
            field=models.NullBooleanField(db_index=True),
        ),
    ]
