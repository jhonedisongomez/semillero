# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 16:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('semilla', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semilla',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 8, 16, 49, 45, 103871, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='semillapersona',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 8, 16, 49, 45, 104301, tzinfo=utc)),
        ),
    ]
