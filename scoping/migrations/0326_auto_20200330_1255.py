# Generated by Django 2.2.9 on 2020-03-30 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0325_auto_20200330_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='docusercat',
            name='baseline_year_2',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='docusercat',
            name='observation_year_2',
            field=models.IntegerField(null=True),
        ),
    ]
