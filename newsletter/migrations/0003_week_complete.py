# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20150707_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='complete',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
