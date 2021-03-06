# Generated by Django 4.0.1 on 2022-01-05 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0005_alter_location_latitude_alter_location_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=7, max_digits=18),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=7, max_digits=18),
        ),
    ]
