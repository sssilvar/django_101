# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-12 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
