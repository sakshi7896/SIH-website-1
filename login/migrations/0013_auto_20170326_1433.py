# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-26 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20170325_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='city_ids',
            new_name='headquaters',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='district_foreign_id',
            new_name='state_foreign_id',
        ),
        migrations.AlterField(
            model_name='district',
            name='id',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]