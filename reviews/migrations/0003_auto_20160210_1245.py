# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 17:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20160210_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='affiliate_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]