# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-12 01:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0023_auto_20160731_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyAccountBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=7)),
                ('is_name_on_bill', models.BooleanField()),
                ('is_address_on_bill', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='energyaccount',
            name='is_residential',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='energyaccountbill',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.EnergyAccount'),
        ),
    ]
