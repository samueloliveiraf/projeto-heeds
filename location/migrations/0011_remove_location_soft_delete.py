# Generated by Django 4.0.1 on 2022-01-06 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0010_location_soft_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='soft_delete',
        ),
    ]