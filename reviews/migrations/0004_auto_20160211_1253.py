# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-11 17:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20160210_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productreview',
            old_name='review',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='productreview',
            old_name='name',
            new_name='title',
        ),
    ]