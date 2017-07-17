# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 05:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20170714_0516'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='my_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
