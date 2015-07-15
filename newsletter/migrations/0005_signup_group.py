# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_subscriber_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='group',
            field=models.CharField(db_index=True, max_length=24, default=''),
            preserve_default=False,
        ),
    ]
