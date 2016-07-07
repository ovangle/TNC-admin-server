# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 01:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_energyaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='energy_account',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='member.EnergyAccount'),
            preserve_default=False,
        ),
    ]
