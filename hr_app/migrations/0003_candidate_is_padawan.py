# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_app', '0002_datamigration'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='is_padawan',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]