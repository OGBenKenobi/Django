# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-21 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='None', max_length=1000),
        ),
    ]
