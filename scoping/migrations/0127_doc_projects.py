# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0126_auto_20170801_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='projects',
            field=models.ManyToManyField(through='scoping.DocProject', to='scoping.Project'),
        ),
    ]
