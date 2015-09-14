# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0008_auto_20150911_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='convio_active',
            field=models.NullBooleanField(db_index=True),
            preserve_default=True,
        ),
    ]
