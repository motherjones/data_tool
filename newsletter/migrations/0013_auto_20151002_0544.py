# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    def f(apps, schema_editor):
        # We can't import the Person model directly as it may be a newer
        # version than this migration expects. We use the historical version.
        Subscriber = apps.get_model("newsletter", "Subscriber")
        active = Subscriber.objects.filter(active=True)
        active.update({
            'in_count': 0,
            'out_count': -1,
        })
        inactive = Subscriber.objects.filter(active=False)
        inactive.update({
            'in_count': -1,
            'out_count': -1,
        })
        empty = Subscriber.objects.filter(active__isnull=True)
        inactive.update({
            'in_count': -1,
            'out_count': 0,
        })
    dependencies = [
        ('newsletter', '0012_auto_20151002_0543'),
    ]

    operations = [migrations.RunPython(f)]
