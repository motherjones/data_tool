# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_auto_20150827_2043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='active',
            new_name='accept_email',
        ),
    ]
