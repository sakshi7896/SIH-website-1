# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-31 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0019_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schooluser',
            name='numOfStudents',
        ),
        migrations.AddField(
            model_name='schooluser',
            name='numOfStudentsPrimary',
            field=models.IntegerField(default=203),
        ),
        migrations.AddField(
            model_name='schooluser',
            name='numOfStudentsSeconadry',
            field=models.IntegerField(default=279),
        ),
        migrations.AddField(
            model_name='schooluser',
            name='numOfStudentsSenior',
            field=models.IntegerField(default=429),
        ),
    ]