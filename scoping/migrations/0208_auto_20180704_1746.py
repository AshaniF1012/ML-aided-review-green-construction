# Generated by Django 2.0.5 on 2018-07-04 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0207_auto_20180619_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docauthinst',
            name='institution',
            field=models.TextField(db_index=True, verbose_name='Institution Name'),
        ),
    ]
