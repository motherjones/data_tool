# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0009_auto_20150716_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email_domain',
            field=models.CharField(max_length=100, db_index=True),
        ),
    ]
