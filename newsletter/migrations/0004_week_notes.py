# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0003_auto_20150814_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
