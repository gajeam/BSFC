# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-09 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
