# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-09 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0043_wosarticle_iss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='UT',
            field=models.CharField(db_index=True, max_length=120, primary_key=True, serialize=False),
        ),
    ]
