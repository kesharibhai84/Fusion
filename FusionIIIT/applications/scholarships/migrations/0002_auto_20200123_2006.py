# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-23 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previous_winner',
            name='year',
            field=models.IntegerField(default=2020),
        ),
    ]
