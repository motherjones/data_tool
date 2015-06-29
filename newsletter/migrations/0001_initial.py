# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('email', models.CharField(max_length=40)),
                ('email_domain', models.CharField(max_length=24)),
                ('active', models.BooleanField()),
                ('date', models.DateField()),
                ('bounces', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
