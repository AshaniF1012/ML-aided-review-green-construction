# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-20 12:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0152_auto_20171020_1207'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkProperties_copy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(null=True)),
                ('fvalue', models.FloatField(null=True)),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.Doc_2')),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.Network')),
            ],
        ),
    ]
