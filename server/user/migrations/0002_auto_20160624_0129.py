# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 01:29
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='permissions',
        ),
        migrations.RemoveField(
            model_name='usergroup',
            name='permissions',
        ),
        migrations.AddField(
            model_name='user',
            name='_extra_permissions',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='_permissions',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
