# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-27 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0009_auto_20160820_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='eapavoucher',
            name='first_voucher_id',
            field=models.IntegerField(default=100000),
            preserve_default=False,
        ),
    ]
