# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-10 18:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20180510_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickevent',
            name='cut_url',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shorter.CutURL'),
        ),
    ]
