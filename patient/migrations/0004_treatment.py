# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-21 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_charged', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now=True)),
                ('symptoms', models.CharField(max_length=500, null=True)),
                ('diagnosis', models.CharField(max_length=1000)),
                ('recommendations', models.CharField(max_length=1000, null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
