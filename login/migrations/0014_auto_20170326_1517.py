# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-26 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_auto_20170326_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='district_foreign_id',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.CharField(max_length=9, primary_key=True, serialize=False),
        ),
    ]