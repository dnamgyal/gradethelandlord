# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-10 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradethelandlord', '0006_auto_20180410_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]
