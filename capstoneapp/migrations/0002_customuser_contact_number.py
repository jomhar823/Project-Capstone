# Generated by Django 4.2.6 on 2023-10-29 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstoneapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
