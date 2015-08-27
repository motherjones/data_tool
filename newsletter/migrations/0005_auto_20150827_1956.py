# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_week_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='net_active_change',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='week',
            name='new_active',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='week',
            name='new_emails_count',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='week',
            name='date',
            field=models.DateField(unique=True, db_index=True),
        ),
    ]
