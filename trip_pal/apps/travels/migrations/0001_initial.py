# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-27 01:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('plan', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_trip', to='login_registration.User')),
                ('trip_members', models.ManyToManyField(related_name='joined_trips', to='login_registration.User')),
            ],
        ),
    ]