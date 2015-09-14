# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_auto_20150911_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriber',
            old_name='accept_email',
            new_name='active',
        ),
    ]
