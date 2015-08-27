# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_auto_20150827_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='active_to_inactive_count',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='week',
            name='inactive_to_active_count',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
