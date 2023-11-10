# Generated by Django 2.0.5 on 2018-10-05 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0238_auto_20181005_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='sbscategory',
            field=models.ManyToManyField(to='scoping.SBSDocCategory'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='category',
            field=models.ManyToManyField(db_index=True, to='scoping.Category'),
        ),
    ]
