# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_userreview_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='user_review',
            field=models.ManyToManyField(to='reviews.UserReview'),
        ),
    ]
