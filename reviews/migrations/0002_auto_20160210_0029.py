# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 05:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='affiliate_link',
            field=models.URLField(null=True),
        ),
    ]