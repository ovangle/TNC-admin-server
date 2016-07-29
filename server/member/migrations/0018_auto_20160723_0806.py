# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0017_auto_20160719_0226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberpartner',
            name='_member',
        ),
        migrations.RemoveField(
            model_name='memberpartner',
            name='partner_ptr',
        ),
        migrations.RemoveField(
            model_name='nonmemberpartner',
            name='carer',
        ),
        migrations.RemoveField(
            model_name='nonmemberpartner',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='nonmemberpartner',
            name='income',
        ),
        migrations.RemoveField(
            model_name='nonmemberpartner',
            name='name',
        ),
        migrations.RemoveField(
            model_name='nonmemberpartner',
            name='partner_ptr',
        ),
        migrations.RemoveField(
            model_name='member',
            name='is_partnered',
        ),
        migrations.AlterField(
            model_name='member',
            name='partner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.Member'),
        ),
        migrations.DeleteModel(
            name='MemberPartner',
        ),
        migrations.DeleteModel(
            name='NonMemberPartner',
        ),
        migrations.DeleteModel(
            name='Partner',
        ),
    ]
