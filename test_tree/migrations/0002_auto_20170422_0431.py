# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 04:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_tree', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='id',
        ),
        migrations.AddField(
            model_name='genre',
            name='node_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
