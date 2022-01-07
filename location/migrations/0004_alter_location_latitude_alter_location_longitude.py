# Generated by Django 4.0.1 on 2022-01-05 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_remove_location_lat_remove_location_lon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=5, max_digits=18),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=5, max_digits=18),
        ),
    ]
