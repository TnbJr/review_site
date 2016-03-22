# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-21 19:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cannabis_type',
            field=models.CharField(choices=[('Sativa', 'Sativa'), ('Indica', 'Indica'), ('Hybrid', 'Hybrid')], default='Sativa', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2016, 3, 21, 19, 23, 52, 332335, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'M'), ('Female', 'F'), ('N/A', 'Does it really matter?')], default='M', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
