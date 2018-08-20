# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-20 20:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20180817_1929'),
        ('records', '0012_auto_20180801_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercreditpathway',
            name='pathway',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Pathway'),
        ),
    ]
