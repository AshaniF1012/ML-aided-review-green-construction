# Generated by Django 2.2 on 2019-06-04 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0284_auto_20190604_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='intervention',
            name='co2_savings_calculated',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='field_group',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='studyeffect',
            name='control_type',
            field=models.TextField(default='-999', null=True),
        ),
        migrations.AddField(
            model_name='studyeffect',
            name='number_of_observations',
            field=models.IntegerField(default=-999, null=True),
        ),
        migrations.AddField(
            model_name='studyeffect',
            name='underlying_source',
            field=models.TextField(default='-999', null=True, verbose_name='Source of underlying data'),
        ),
    ]