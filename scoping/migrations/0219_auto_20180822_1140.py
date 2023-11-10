# Generated by Django 2.0.5 on 2018-08-22 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0218_auto_20180822_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyeffect',
            name='aggregation_level',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='coefficient',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='coefficient_sd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='control_definition',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='control_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='control_sd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='diff_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='pooled_sd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='test_statistic_df',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='total_sample_size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='treated_mean',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='treated_sd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studyeffect',
            name='treatment_sample_size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]