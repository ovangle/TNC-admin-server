# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-19 03:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0025_auto_20160815_0203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='energyaccount',
            name='is_residential',
        ),
    ]
