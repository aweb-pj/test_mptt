# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_tree', '0003_auto_20170422_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='material',
            field=models.FileField(null=True, upload_to='materials/'),
        ),
    ]