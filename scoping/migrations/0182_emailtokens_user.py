# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-20 09:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scoping', '0181_auto_20171215_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtokens',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
