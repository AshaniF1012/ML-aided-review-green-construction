# Generated by Django 2.2.9 on 2020-03-04 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0316_project_criteria'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='no_relevance',
            field=models.BooleanField(default=False),
        ),
    ]
