# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_auto_20160814_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='quantity',
            new_name='quantity_sold',
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
