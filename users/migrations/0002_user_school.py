# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-07 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.CharField(max_length=255, null=True, verbose_name='目前的学校'),
        ),
    ]
