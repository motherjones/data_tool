# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0010_auto_20150923_2057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='week',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='signup',
            name='in_count',
            field=models.IntegerField(blank=True, db_index=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='signup',
            name='out_count',
            field=models.IntegerField(blank=True, db_index=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='signup',
            name='subsource',
            field=models.CharField(default='', max_length=200, db_index=True),
            preserve_default=False,
        ),
    ]
