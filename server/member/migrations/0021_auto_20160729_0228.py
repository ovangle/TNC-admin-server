# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import ext.django.fields
import member.basic.gender


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0020_remove_carer_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependent',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='dependent',
            name='gender',
            field=ext.django.fields.EnumField(choices=[('not_disclosed', 'NOT_DISCLOSED'), ('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], enum_type=member.basic.gender.Gender, max_length=32, null=True),
        ),
    ]
