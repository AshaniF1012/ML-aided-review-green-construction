# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-13 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0137_auto_20171013_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='first_author',
            field=models.TextField(null=True, verbose_name='First Author'),
        ),
    ]
