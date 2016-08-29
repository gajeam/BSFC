# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-29 01:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('revenue', '0001_initial'),
        ('cost', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('label', models.CharField(max_length=100, null=True)),
                ('price', models.FloatField()),
                ('price_type', models.CharField(choices=[(b'FI', 'fixed'), (b'P/U', 'per_unit')], default=b'FI', max_length=100, null=True)),
                ('unit_name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[(b'B', 'Bakery'), (b'G', 'Grocery'), (b'BU', 'Bulk'), (b'BSFC', 'BSFC'), (b'P', 'Produce'), (b'H&B', 'Health & Beauty'), (b'H', 'Household'), (b'BEV', 'Beverage'), (b'C', 'Chill'), (b'G&G', 'Grab & Go'), (b'FR', 'Frozen')], default=None, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cost', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cost.Cost')),
                ('revenue', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='revenue.Revenue')),
            ],
        ),
    ]
