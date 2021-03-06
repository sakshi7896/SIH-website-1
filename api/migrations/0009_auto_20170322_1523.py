# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-22 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20170320_1012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='latitude',
            new_name='latitude_1',
        ),
        migrations.RenameField(
            model_name='attendance',
            old_name='longitude',
            new_name='latitude_2',
        ),
        migrations.AddField(
            model_name='attendance',
            name='latitude_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='latitude_4',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='longitude_1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='longitude_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='longitude_3',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='longitude_4',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
