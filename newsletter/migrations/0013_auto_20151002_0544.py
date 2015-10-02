# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    def f(apps, schema_editor):
        # We can't import the Person model directly as it may be a newer
        # version than this migration expects. We use the historical version.
        Subscriber = apps.get_model("newsletter", "Subscriber")
        for subscriber in Subscriber.objects.all():
            if subscriber.active != None:
                subscriber.in_count = int(subscriber.active)
            else:
                subscriber.in_count = 0
            subscriber.save()
    dependencies = [
        ('newsletter', '0012_auto_20151002_0543'),
    ]

    operations = [migrations.RunPython(f)]
