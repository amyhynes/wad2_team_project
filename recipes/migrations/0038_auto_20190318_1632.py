# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-18 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0037_auto_20190313_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chef',
            name='bio',
            field=models.TextField(blank=True, default='Hello! I enjoy making food the opportunity to upload recipes, share tips, and explore recipes on this website!'),
        ),
    ]
