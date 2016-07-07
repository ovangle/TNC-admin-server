# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import ext.django.fields
import member.membership_term.term_type


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_auto_20160704_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', ext.django.fields.EnumField(choices=[('temporary', 'TEMPORARY'), ('associate', 'ASSOCIATE'), ('general', 'GENERAL')], enum_type=member.membership_term.term_type.MembershipTermType, max_length=32)),
                ('joined', models.DateTimeField()),
                ('renewed', models.DateTimeField()),
                ('expires', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='term',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='member.MembershipTerm'),
        ),
    ]
