# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 14:27
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Semilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('activo', models.BooleanField(default=True)),
                ('version', models.IntegerField(default=1)),
                ('updated', models.DateTimeField(default=datetime.datetime(2017, 11, 8, 14, 27, 22, 229152, tzinfo=utc))),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semilla_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SemillaPersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disponible', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(default=datetime.datetime(2017, 11, 8, 14, 27, 22, 229582, tzinfo=utc))),
                ('fk_semilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semilla_per_semilla', to='semilla.Semilla')),
                ('fk_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semilla_per_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
