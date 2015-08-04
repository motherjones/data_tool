# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('email', models.CharField(max_length=100, db_index=True, unique=True)),
                ('email_domain', models.CharField(max_length=100, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('code', models.CharField(max_length=200, db_index=True)),
                ('created', models.DateTimeField(db_index=True)),
                ('signup_url', models.URLField(max_length=400, db_index=True)),
                ('group', models.CharField(max_length=200, db_index=True)),
                ('email', models.ForeignKey(to='newsletter.Email')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('active', models.NullBooleanField(db_index=True)),
                ('bounces', models.IntegerField(db_index=True)),
                ('updated_on', models.DateTimeField()),
                ('email', models.ForeignKey(to='newsletter.Email')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
