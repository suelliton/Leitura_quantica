# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quantic', '0006_auto_20170420_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.CharField(blank=True, default="{% static 'images/user-icon.jpg' %}", max_length=30),
        ),
    ]
