# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-10 12:31
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0110_doc_k'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='k',
            field=models.IntegerField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='wosarticle',
            name='cr',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None, verbose_name='Cited References'),
        ),
    ]
