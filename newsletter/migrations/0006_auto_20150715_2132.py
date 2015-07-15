# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_signup_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='code',
            field=models.CharField(max_length=40, db_index=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='group',
            field=models.CharField(max_length=40, db_index=True),
        ),
    ]
