# Generated by Django 2.2.9 on 2020-04-17 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0330_auto_20200417_1314'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='doc',
            name='gin_trgm_idx',
        ),
    ]
