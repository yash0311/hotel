# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-23 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='expedia_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='goibibo_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_website_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]