# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='weChat',
            field=models.CharField(blank=True, default=None, max_length=30, null=True),
        ),
    ]