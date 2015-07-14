# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=40, unique=True, db_index=True)),
                ('code', models.CharField(max_length=24, db_index=True)),
                ('created', models.DateTimeField(db_index=True)),
                ('signup_url', models.URLField(db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('email_domain', models.CharField(max_length=24, db_index=True)),
                ('active', models.BooleanField(db_index=True)),
                ('bounces', models.IntegerField(db_index=True)),
                ('last_updated', models.DateField(db_index=True)),
                ('signup', models.ForeignKey(to='newsletter.Signup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateField(unique=True)),
                ('complete', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='week',
            field=models.ForeignKey(to='newsletter.Week'),
            preserve_default=True,
        ),
    ]
