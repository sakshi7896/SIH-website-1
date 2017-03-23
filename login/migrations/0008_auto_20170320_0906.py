# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-20 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20170319_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schooluser',
            old_name='geo_coord',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='schooluser',
            name='location',
        ),
        migrations.AddField(
            model_name='schooluser',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schooluser',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]