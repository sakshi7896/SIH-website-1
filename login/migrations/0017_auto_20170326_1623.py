# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-26 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0016_auto_20170326_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schooluser',
            name='numOfStudents',
            field=models.IntegerField(blank=True, default=100),
        ),
        migrations.AlterField(
            model_name='schooluser',
            name='numOfTeachers',
            field=models.IntegerField(blank=True, default=10),
        ),
    ]
