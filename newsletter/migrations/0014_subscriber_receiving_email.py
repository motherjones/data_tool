# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0013_auto_20151002_0544'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='receiving_email',
            field=models.BooleanField(default=True, db_index=True),
            preserve_default=True,
        ),
    ]
