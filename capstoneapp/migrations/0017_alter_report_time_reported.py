# Generated by Django 4.2.6 on 2023-11-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstoneapp', '0016_alter_report_latitude_alter_report_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='time_reported',
            field=models.TimeField(),
        ),
    ]
