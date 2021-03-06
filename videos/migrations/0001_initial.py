# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-09 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('draft', models.BooleanField(default=False)),
                ('published', models.DateTimeField()),
                ('source', models.URLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('categories', models.CharField(choices=[('video-reviews', 'Reviews'), ('video', 'Video')], default='Video', max_length=50)),
                ('category_slug', models.SlugField()),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
