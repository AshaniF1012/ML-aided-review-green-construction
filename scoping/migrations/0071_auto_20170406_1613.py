# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-06 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0070_merge_20170406_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docrel',
            name='indb',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='docrel',
            name='sametech',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='docrel',
            unique_together=set([('seed', 'text')]),
        ),
    ]