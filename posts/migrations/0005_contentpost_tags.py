# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-20 00:51
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('posts', '0004_auto_20160319_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpost',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]