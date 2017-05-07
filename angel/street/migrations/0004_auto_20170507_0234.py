# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-07 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('street', '0003_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.TextField(default=1234567891, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.FileField(default='SOME STRING', upload_to=b''),
        ),
    ]