# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-04 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuturl',
            name='shortCode',
            field=models.CharField(default='cutLink', max_length=15),
            preserve_default=False,
        ),
    ]