# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_week_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.CharField(max_length=40, db_index=True),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email_domain',
            field=models.CharField(max_length=24, db_index=True),
        ),
    ]
