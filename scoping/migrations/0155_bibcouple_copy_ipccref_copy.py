# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-20 12:30
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import scoping.models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0154_auto_20171020_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='BibCouple_copy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cocites', models.IntegerField(default=0, verbose_name="DOC")),
                ('doc1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='node1', to='scoping.Doc_2')),
                ('doc2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='node2', to='scoping.Doc_2')),
            ],
        ),
        migrations.CreateModel(
            name='IPCCRef_copy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authors', models.TextField()),
                ('year', models.IntegerField()),
                ('text', models.TextField()),
                ('words', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), null=True, size=None)),
                ('chapter', models.TextField(null=True)),
                ('ar', models.ManyToManyField(to='scoping.AR')),
                ('doc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoping.Doc_2')),
                ('wg', models.ManyToManyField(to='scoping.WG')),
            ],
        ),
    ]
