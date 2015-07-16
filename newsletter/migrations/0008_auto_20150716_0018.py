# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_auto_20150715_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='signup_url',
            field=models.URLField(db_index=True, max_length=400),
        ),
    ]
