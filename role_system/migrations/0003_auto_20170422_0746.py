# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('role_system', '0002_auto_20170422_0738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher_id',
            new_name='student_id',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='student_id',
            new_name='teacher_id',
        ),
    ]
