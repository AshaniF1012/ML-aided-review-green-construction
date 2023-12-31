# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-24 09:26
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0085_ipccref'),
    ]

    operations = [
        migrations.CreateModel(
            name='AR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ar', models.IntegerField(unique=True)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wg', models.IntegerField()),
                ('ar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoping.AR')),
            ],
        ),
        migrations.AddField(
            model_name='ipccref',
            name='doc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoping.Doc'),
        ),
        migrations.AddField(
            model_name='ipccref',
            name='words',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None),
        ),
        migrations.RemoveField(
            model_name='ipccref',
            name='ar',
        ),
        migrations.RemoveField(
            model_name='ipccref',
            name='wg',
        ),
        migrations.AddField(
            model_name='ipccref',
            name='ar',
            field=models.ManyToManyField(to='scoping.AR'),
        ),
        migrations.AddField(
            model_name='ipccref',
            name='wg',
            field=models.ManyToManyField(to='scoping.WG'),
        ),
    ]
