# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0014_subscriber_receiving_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='query_complete',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
