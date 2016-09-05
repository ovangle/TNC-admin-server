# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-29 02:06
from __future__ import unicode_literals

import activity.voucher.eapa_voucher_book
import django.contrib.postgres.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0010_eapavoucher_first_voucher_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eapavoucher',
            name='first_voucher_id',
        ),
        migrations.AddField(
            model_name='eapavoucher',
            name='voucher_books',
            field=django.contrib.postgres.fields.ArrayField(base_field=activity.voucher.eapa_voucher_book.EAPAVoucherBookField(), default=list, size=None),
        ),
    ]
