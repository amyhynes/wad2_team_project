# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-20 22:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20190220_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chef',
            name='id',
        ),
        migrations.AlterField(
            model_name='chef',
            name='username',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]