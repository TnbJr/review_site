# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-09 16:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('draft', models.BooleanField(default=False)),
                ('published', models.DateTimeField()),
                ('source', models.URLField(blank=True, null=True)),
                ('affiliate_link', models.URLField(blank=True, null=True)),
                ('categories', models.CharField(choices=[('Desktop Vaporizer', 'Desk'), ('Handheld Vaporizer', 'Hand'), ('Other', 'Other')], max_length=50)),
                ('featured', models.BooleanField(default=False)),
                ('category_slug', models.SlugField()),
                ('convenience', models.CharField(blank=True, max_length=100, null=True)),
                ('concentrate_only', models.CharField(blank=True, max_length=100, null=True)),
                ('product_dimensions', models.CharField(blank=True, max_length=100, null=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.ProductReview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
