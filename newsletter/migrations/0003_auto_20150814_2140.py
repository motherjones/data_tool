# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_signup_is_first'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='is_first',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]
