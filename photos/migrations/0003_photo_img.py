# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-13 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_photo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='img',
            field=models.ImageField(default='', upload_to='photos/'),
            preserve_default=False,
        ),
    ]
