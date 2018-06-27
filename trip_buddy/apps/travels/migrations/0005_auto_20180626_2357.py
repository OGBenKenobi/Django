# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-26 23:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0004_schedule_trip_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_trips', to='login_register.User'),
        ),
    ]