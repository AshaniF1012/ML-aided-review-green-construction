# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-20 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0119_journalabbrev'),
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('type', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('query', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.Query')),
            ],
        ),
        migrations.RemoveField(
            model_name='networkproperties',
            name='degree',
        ),
        migrations.RemoveField(
            model_name='networkproperties',
            name='eigen_cent',
        ),
        migrations.RemoveField(
            model_name='networkproperties',
            name='k',
        ),
        migrations.RemoveField(
            model_name='networkproperties',
            name='query',
        ),
        migrations.AddField(
            model_name='networkproperties',
            name='fvalue',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='networkproperties',
            name='value',
            field=models.IntegerField(null=True),
        ),
    ]
