# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 01:05
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import ext.django.fields
import staff.staff_type


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0006_member_energy_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mon_available', models.BooleanField(default=False)),
                ('mon_start', models.TimeField(default=None, null=True)),
                ('mon_end', models.TimeField(default=None, null=True)),
                ('tue_available', models.BooleanField(default=False)),
                ('tue_start', models.TimeField(default=None, null=True)),
                ('tue_end', models.TimeField(default=None, null=True)),
                ('wed_available', models.BooleanField(default=False)),
                ('wed_start', models.TimeField(default=None, null=True)),
                ('wed_end', models.TimeField(default=None, null=True)),
                ('thu_available', models.BooleanField(default=False)),
                ('thu_start', models.TimeField(default=None, null=True)),
                ('thu_end', models.TimeField(default=None, null=True)),
                ('fri_available', models.BooleanField(default=False)),
                ('fri_start', models.TimeField(default=None, null=True)),
                ('fri_end', models.TimeField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StaffInductionSurvey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_previous_experience', models.BooleanField()),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), default=list, size=None)),
                ('personaility_traits', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), default=list, size=None)),
                ('date_available_to_start', models.DateField()),
                ('desired_hours_per_week', models.SmallIntegerField()),
                ('referred_by', models.CharField(max_length=64)),
                ('has_understood_privacy_obligations', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', ext.django.fields.EnumField(choices=[('Admin', 'ADMIN'), ('PermanentStaff', 'STAFF'), ('OfficeVolunteer', 'OFFICE_VOLUNTEER'), ('FoodcareVolunteer', 'FOODCARE_VOLUNTEER'), ('OtherVolunteer', 'OTHER_VOLUNTEER')], enum_type=staff.staff_type.StaffType, max_length=32)),
                ('date_of_birth', models.DateField()),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.Address')),
                ('availability', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staff.Availability')),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.Contact')),
                ('induction_survey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staff.StaffInductionSurvey')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.Name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
