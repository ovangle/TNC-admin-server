# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20160624_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='alias',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
