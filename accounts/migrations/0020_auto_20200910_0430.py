# Generated by Django 3.0.8 on 2020-09-10 04:30

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20200910_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='following_genres',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=25), blank=True, size=None),
        ),
    ]
