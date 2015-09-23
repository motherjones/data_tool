# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from newsletter import models


def update_aggregates(apps, schema_editor):
    for week in models.Week.objects.all():
        week.update_aggregate()

class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0009_subscriber_convio_active'),
    ]

    operations = [migrations.RunPython(update_aggregates)]
