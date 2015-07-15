# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20150714_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='updated_on',
            field=models.DateTimeField(default=datetime.date(2015, 7, 15)),
            preserve_default=False,
        ),
    ]
