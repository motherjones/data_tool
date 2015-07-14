# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20150714_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='email_domain',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='signup',
            name='email_domain',
            field=models.CharField(default='', max_length=24, db_index=True),
            preserve_default=False,
        ),
    ]
