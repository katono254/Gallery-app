# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-04 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20200203_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='greg', upload_to='images/'),
        ),
    ]
