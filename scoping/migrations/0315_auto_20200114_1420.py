# Generated by Django 2.2.2 on 2020-01-14 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoping', '0314_docusercat_tweet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docusercat',
            name='doc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scoping.Doc'),
        ),
    ]
