# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-25 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_attendance_present_presence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
