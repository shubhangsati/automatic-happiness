# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-06 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('street', '0002_auto_20170506_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pic',
            field=models.FileField(default='SOME STRING', upload_to='/profile'),
        ),
    ]