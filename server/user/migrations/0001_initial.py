# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 00:41
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=128, unique=True)),
                ('permissions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), default=list, size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('permissions', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=64), default=list, size=None)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(to='user.UserGroup'),
        ),
    ]
