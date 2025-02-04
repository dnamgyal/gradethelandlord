# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-10 01:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradethelandlord', '0004_auto_20180410_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='apartment_condition',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='2', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='communication_with_your_landlord',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='landlord_helpfulness',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='maintenance_efficiency',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='move_in_condition',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='overall_rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='rent_again',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='1', max_length=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='treatment_by_your_landlord',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=5),
        ),
    ]
