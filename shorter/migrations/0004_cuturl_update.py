# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-04 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0003_auto_20180504_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuturl',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]