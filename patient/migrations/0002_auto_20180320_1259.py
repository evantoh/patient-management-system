# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-20 09:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ['first_name']},
        ),
    ]
