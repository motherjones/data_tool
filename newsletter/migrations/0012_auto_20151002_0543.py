# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0011_auto_20151002_0535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='in_count',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='out_count',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='in_count',
            field=models.IntegerField(db_index=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriber',
            name='out_count',
            field=models.IntegerField(db_index=True, default=0),
            preserve_default=False,
        ),
    ]
