# Generated by Django 4.0.1 on 2022-01-05 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_alter_location_latitude_alter_location_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
