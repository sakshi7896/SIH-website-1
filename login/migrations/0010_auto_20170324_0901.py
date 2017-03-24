# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-24 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20170324_0635'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('city_name', models.CharField(blank=True, max_length=50)),
                ('city_ids', models.CharField(blank=True, max_length=50)),
                ('state_foreign_id', models.CharField(blank=True, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('state_name', models.CharField(blank=True, max_length=50)),
                ('state_ids', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='schooluser',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='schooluser',
            name='city_id',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='schooluser',
            name='state_id',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]