# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantic', '0010_auto_20170422_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image_upload',
            field=models.ImageField(default='/static/images/none.jpg', upload_to='static/images/'),
            preserve_default=False,
        ),
    ]
