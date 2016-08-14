# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_use', models.FloatField(default=0.0, null=True)),
                ('spoilage', models.FloatField(default=0.0, null=True)),
                ('food_prep', models.FloatField(default=0.0, null=True)),
                ('committee', models.FloatField(default=0.0, null=True)),
            ],
        ),
    ]
